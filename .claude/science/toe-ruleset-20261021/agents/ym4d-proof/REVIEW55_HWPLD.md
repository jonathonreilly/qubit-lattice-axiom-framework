Reviewer model: claude-opus-5-5

# REVIEW55_HWPLD — Opus 5.5 re-review of the HW lane (session 6, HW.md §34-§41) and the PLD lane (sessions 6-7, PLD.md §18-§19), plus the earlier reviewers REVIEW_HW_S5 / REVIEW_PLD_S5

UTC start: 2026-10-28T22:12:18Z
Batch: C3. Check-id prefix: `r55h_`. Deliverable (the only lane file written): `$L/REVIEW55_HWPLD.md`
(plus `checks/r55h_*` criteria/scripts when a numeric check is needed; criteria written before the script).
No git commands are run. This file is append-only.

## PRE-STATED (written before any derivation; statements only)

Targets (each gets CONFIRMED / NOT-VERIFIED / REFUTED):

T1  REVIEW_HW_S5's headline "the smallness alarm is false": the HW constants are satisfiable with ~55
    orders of slack, later refined to x3.59e56. (Review of a reviewer; its verdict was banked.)
T2  HW s6: lever (b) REFUTED (a refutation; checked as hard as a theorem).
T3  HW s6: lever (a) "beaten".
T4  The HW/PLD interface defect: (i) that it exists; (ii) the diagnosis "NA-PRICE generates no allowance,
    it only transmits the hypothesis's, so the patch allowance is a clause of the hypothesis"; (iii) that
    the HW repair and the PLD repair ("Proposition PATCH" form) actually match (same hypothesis, same
    allowance, same quantifiers).
T5  The ring price: x17 for the open column, x82 for the closed column; the claim that the closed column
    is what the proof uses; downstream figures quoted "at the x82 ring" (e.g. g^2_CRC) and the reported
    mis-pointer (a later file citing HW l.2006, the x17 row, for the x82 figure at l.2007).
T6  PLD s6: (E2^F)'s law conversion "closed and priced".
T7  PLD s7: (CEM-2) "dissolved".
T8  PLD s7: (LCR) "restated past its own impossibility".
T9  SYMBOLS.md defect claim: PLD l.1098 (repeated l.1206, l.1244, l.1260) m_tau = 3 is wrong; the depth is
    66/90/122 at RLARGE's threshold, because l.1097 substitutes c_1 for eta_1/eps_1, constant only for one
    of the eta_1's.
T10 SYMBOLS.md defect claim: HW l.604 a_bad ~ 5e-23/C_D^4 should be ~ 5.01e-22/C_D^4 (x9), because HW
    l.183 quotes a theta_0 that SQ corrects four lines later.
T11 REVIEW_HW_S5's other banked verdicts (beyond T1), each re-judged.
T12 REVIEW_PLD_S5's banked verdicts, each re-judged.
T13 Every PROVEN / PROVEN-HERE / CLOSED claim in HW §34-§41 and PLD §18-§19 not already in T2-T8.
T14 Every REFUTED / FALSE / struck verdict in those sections against earlier banked items.
T15 Every decision-changing number in those sections: arithmetic, currency (decades of what, against which
    ceiling, with which constants frozen), and the value of each symbol it was evaluated at.
T16 The session-6/7 entries of HW_LOG.md and PLD_LOG.md: do their status lines match the sections?
T17 Every CODEX_REVIEW_*.md finding that touches this batch: agree / disagree, per finding.

What counts as a refutation:
- PROVEN / CLOSED / "beaten" / "priced" claims: an explicit counterexample; a false load-bearing step (an
  inequality failing at the stated quantifier, a "constant" that is not constant, an identity that does not
  hold); a hidden input the conclusion needs that is not in the stated hypothesis list (then REFUTED as
  stated); or a symbol in a load-bearing comparison that denotes a different object than the one the
  claim needs (systemic defect 1), or a value quoted at a stale constant (systemic defect 2).
- REFUTED / FALSE / "smallness alarm is false" verdicts: the verdict is itself refuted if its counterexample
  or witness does not satisfy the hypotheses of the statement it judges, if it judges a different statement
  (collision / different quantifier / different ceiling), or if its arithmetic is wrong by more than its
  stated rounding in a way that flips the verdict.
- Numbers: an exact-rational (and rigorous rational-interval for logarithms) recomputation that differs from
  the quoted value beyond the quoted rounding is a REFUTATION with the corrected value; a currency mismatch
  (wrong ceiling / constants not frozen as claimed) is a REFUTATION of the use, even when the arithmetic is right.
- "Both repairs match" (T4.iii): refuted by any difference in the hypothesis clause, the allowance's placement,
  or a quantifier between the two lanes' stated forms.
- "The closed column is what the proof uses" (T5): refuted if the consuming statement in the proof uses the
  open-column quantity.
- SYMBOLS.md claims (T9, T10): CONFIRMED only if the cited lines (located by string) say what SYMBOLS says and
  the corrected value recomputes; REFUTED if the original line is right in its own scope (e.g. the symbol there
  denotes the object for which the quoted value holds).
- A check that could not have failed decides nothing; such a gate is reported, not counted as evidence.
- A status line (file or log) that says more than the section derives is a REFUTATION of the status line.

(PRE-STATED ends here. Everything below was written after it; first derivation 22:13 UTC.)

## Inputs read (read-only), as the files stand on disk now
- HW.md (254211 bytes, 2411 lines = HW_LOG's session-6 close): §34-§41 (l.1737-2411) in full; for definitions §13.1
  (l.607-640), §24.1 (l.1191-1200), §29-§30.7 (l.1425-1665); l.180-186, l.600-606, l.826.
- PLD.md (389932 bytes, 3705 lines = PLD_LOG's session-7 close): §18 (l.1968-2932) and §19 (l.2933-3705) in full; §16.6-§16.7
  (l.1445-1500); l.1085-1102, l.1206, l.1244, l.1260.
- REVIEW_HW_S5.md (714 lines) and REVIEW_PLD_S5.md (561 lines) in full. HW_LOG.md session 6; PLD_LOG.md sessions 6-7.
- Context, located by grep: RLARGE.md l.58-72, l.125-135, l.185-192, l.605-620, l.826-834, l.905, l.973; SF.md l.1-40,
  l.2078-2094; HIST.md l.545-556; SQ.md l.186-232, l.290-298; SYMBOLS.md §2.3-§2.5, §4.4-§4.5, l.835-858; HANDOFF.md l.1-190;
  PROOF.md l.85-97, l.6900-6925; EPS1_SWEEP.md / EPS1_EXEC.md / SESSION24_RESULTS.md / SESSION25_RESULTS.md at the grep hits named.
- Codex reviews: CODEX_REVIEW_SYMBOLS.md (275 lines; ends with a "Stdout summary" — complete) and CODEX_REVIEW_DECADES.md
  (ends with its verdict table — complete) are the only two that touch this batch (grep of all twelve CODEX_REVIEW_* files
  for HW/PLD/ring/CEM/LCR/m_τ/Δ_sh strings; the other ten have no hit).

## Checks run (criteria written and hashed BEFORE each script; exact arithmetic; no floats in any verdict)
| id | criteria (md5) | script | result |
|---|---|---|---|
| r55h_geo | checks/r55h_geo_criteria.md (137c0dc5…, 22:41:10Z) | checks/r55h_geo.py → r55h_geo_out.txt, 1.4 s, empty stderr | G-A PASS; G-A3 REFUTED (the sentence); **G-B REFUTED (PLD's depth-free Δ_sh)**; G-B3 control behaves (bounded, 81); G-C1, G-C2, G-C4 PASS |
| r55h_arith | checks/r55h_arith_criteria.md (f785d28f…, 22:41:53Z) | checks/r55h_arith.py → r55h_arith_out.txt, 7.7 s, empty stderr | A1 PASS; A2 PASS; **A3 FAIL on two printed figures** (both immaterial, see F7); A5, A6, A7-reproduction, A8-reproduction PASS; records A4, A7, A8 |
| r55h_ring | checks/r55h_ring_criteria.md (1d8c6e0e…, 22:46:59Z) | same script (records R1-R4 only; no thresholds, because the formulas are derived in this review) | records |
Could each gate fail? G-A: yes (any E(M) ≠ 27M+55); G-A3: yes (either answer was reportable); G-B: yes, and its control G-B3
ran the identical code path at the all-ones position, where the excess stays 81 for every depth, so G-B's growth is a
property of the position, not of the code; G-C1/G-C2/G-C4: yes (set (in)equalities on 200 seeded samples each, positions
including all-ones base-3 neighbourhoods). A1-A3: yes (each printed figure was compared at its printed precision; two
failed). A5: yes, with the ε_1 = 2 control reproducing REVIEW_PLD_S3's independently recorded (5,7,10).

---

# FINDINGS

Notation: "line" = current line of the named file; strings are quoted so a drifted citation can be re-found.

## F1 (T1) REVIEW_HW_S5's headline "the smallness alarm is false" — **CONFIRMED** (with a currency argument the review did not give)
*Where:* REVIEW_HW_S5 "S5-11 (CONFIRMED, and the answer is YES)", "S5-13 … the breach does not bind against DX′"; HW §35.7 (iii)
"exceeds it by **×3.5855·10⁵⁶**"; HANDOFF "WITHDRAWN … slack ×3.59e56".
- *g-independence (S5-11).* Re-traced from the definitions: g²_CRC = a/(b_n + aR + log(12800C_ℓ)) (HW l.1639) with
  a = θa_bad, a_bad = c_prε_1², ε_1 fixed at a g-free ceiling (RLARGE l.71-72), θ constrained only by
  max{6θ, 24θ}(1 + 2Rg_K²) < 1 (which relaxes as g → 0); b_n, b_D, c_att geometric × c_+; C_ℓ = (1 − λ_*)^{-3n_int/2}C_fc with
  λ_* ≤ 6θ(1 + 2Rg_K²). No term grows as g → 0. **CONFIRMED** (conditional, as the review says, on node A's constants existing).
- *Arithmetic (r55h_arith A3).* s5: g²_CRC/2.5e-152 = 1.959157563e55 (review "1.96e55" ✓, w6 "1.9592e55" ✓); s6 ×17: 3.585504608e56 ✓;
  break-even c_+ = 6.095412529e57 ✓.
- *Currency — symbol collision on g_0 (systemic defect 1).* DX′'s ceiling is stated on **u_0 = 1/g_0², the stage-0 coupling**
  (SF §0: "At stage 0 the U_0-integrand is e^{-u_0Σ_ps(U_0(p))}…"; SF l.2083 "summing over patterns needs a′/g_0² ≥ C_Ω|Ω_B| + 1").
  (S2) bounds **g_K, the coarsest coupling**, and by (F_R) g_K is the LARGEST coupling of the chain. RLARGE Theorem RLF v3
  (l.187-189) uses g_0 for a third object, a threshold "g_K ≤ g_0" uniform in K. REVIEW_HW_S5, HW §35.7 (iii) and
  RLARGE l.617-618 all compare a g_K-ceiling with the stage-0 g_0-ceiling without saying why they are comparable.
  *The comparison is nevertheless valid, for this reason:* the threshold must work for every K, in particular K = 1, where the
  upper bracket of (F-3) (RLARGE l.550: u_j − u_n ≤ β_+(n − j)log L + R) gives u_0 ≤ u_1 + β_+log L + R; so DX′'s u_0-ceiling
  forces g_1² ≲ 2.5·10⁻¹⁵²/C_Ω up to an O(β_+log L + R) shift in u. Hence the uniform threshold is already ≲ the DX′ value and
  any g_K-ceiling above it — (S2)'s included — costs nothing. With that argument supplied, the headline stands.
- *The figure is stale but the verdict is not.* "×3.59·10⁵⁶" is (S2) at the ×17 ring. Across every convention in this batch
  (ring ×1 / ×17 / ×82; HIST as written / H-geo′ adopted) the HW-route binding ceiling min{(S2), REL-boot, HIST-sum} lies
  **55.29-57.78 decades** above 2.5·10⁻¹⁵² (r55h_arith A4, R4). It does not bind provided c_+ ≲ 10⁵⁵·C_Ω — i.e. the open risk
  is c_A, as the review says.

## F2 (T2) HW s6 "lever (b) refuted" — Proposition SH-neg — **CONFIRMED**; one sentence in it **REFUTED**
*Where:* HW l.1908 "Proposition SH-neg (no additive form exists)"; l.1940 and l.2283 (§40 W1 (b)) "π^r(y) stays at distance 1
from π^r(z) for ever"; l.1901 "the samples force a multiplicative factor ≥ 5.714".
- *Re-derived by hand.* ζ = (3^{M+1}−1)/2 has all base-3 digits 1, so ζ_r := π^r(ζ) = (3^{M+1−r}−1)/2 ≡ 1 (mod 3) for r ≤ M and
  {ζ_r − 1, ζ_r, ζ_r + 1} all project to ζ_{r+1}: P's 1D shadow is the 3-set C_r for every r ≥ 1. η = ζ + 8 = 3(ζ_1 + 3) gives
  Σ(η) = {ζ_1+2, ζ_1+3, ζ_1+4} (disjoint from C_1), Σ²(η) = {ζ_2, ζ_2+1, ζ_2+2}, and from r = 3 the invariant 4-set
  D_r = {ζ_r−1, …, ζ_r+2} (π(D_r) = {ζ_{r+1}, ζ_{r+1}+1}). Coordinatewise product: excess 1 (r=0) + 3·27 (r=1) + 27 per level
  (r ≥ 2) = 27M + 55; ratio (108M + 56)/(81M + 1) → 4/3. So no c(ρ) independent of depth and no multiplicative constant
  below 4/3. **The reviewer's conjectured additive form (REVIEW_HW_S5 S5-14 (2)) is false, and the refutation stands.**
- *Exact check (r55h_geo G-A, PASS).* Direct 4D set computation M = 2..7 equals the product reduction; E(M) = 27M + 55 for
  every M = 2..60.
- **REFUTED (the diagnosis sentence).** d_r := π^r(η) − π^r(ζ) = 8, 3, 1, **0, 0, 0, …** (G-A3): ζ_2 + 1 = 3ζ_3 + 2 projects to
  ζ_3. The projections **coincide from r = 3 on**; they do not "stay at distance 1 for ever". Correct statement: the
  projections coincide from r = 3, yet the shadows never merge, because a single cube's shadow depends on its position
  inside the coarse block, not only on its projection. (This makes the reviewer's proposed lemma "π^r(Y) ⊂ N_1(π^r(P)) ⇒
  Σ^{r+c}(P∪Y) = Σ^{r+c}(P)" fail even more plainly: its hypothesis holds from r = 2 with distance 0 from r = 3.)
- **REFUTED (minor, l.1901).** "The samples force a multiplicative factor ≥ 5.714": a ratio ‖P∪Y‖_sh/‖P‖_sh = 5.714 observed at
  one depth with |Y| > 1 forces nothing about C in ‖P∪Y‖_sh ≤ C‖P‖_sh + c|Y|, because c|Y| (c = 320001) absorbs it. Only a
  depth-scaling family forces a lower bound on C; SH-neg's gives 4/3. The "loose by at most ≈ 14" figure is unsupported.

## F3 (T3) HW s6 "lever (a) beaten" — the factor 81 — **CONFIRMED**
*Where:* HW §35.2-§35.5 (Lemmas SH-1, SH-2, COV, Corollary H-geo′, Lemma SH-att′ l.~1870, Lemma COL′ l.~1943).
- SH-1 (Σ^r(X) ⊇ N_1(π^r X)): induction via monotonicity of N_1∘π. ✓
- SH-2 (Σ^r(X) ⊆ N_2(π^r X)): |⌊u/L⌋ − ⌊v/L⌋| ≤ ⌈|u−v|/L⌉ ≤ 1 for |u−v| ≤ 2 ≤ L, so π(N_2 B) ⊆ N_1(π B) and radius 2 is a fixed
  point of B ↦ N_1(π(N_2 B)). ✓ Radius 1 fails (a single cube's Σ² can be a 4-block). ✓ (G1 in w6; my own G-A shows 4-blocks.)
- COV (N_2 = ∪ 2^d translates of N_1; N_3, N_4 = ∪ 3^d translates): the coordinatewise choices of t given in the file cover
  [a−s, a+s] for s = 2, 3, 4. ✓
- SH-att′: case (a) (ℓ_iL^{-r} < 1) — every point of the scaled tree is within Euclidean distance < 1 of the unit box of π^r(z_i),
  so each π^r(y) ∈ N_1(π^r z_i); hence Σ^r(Y_i) ⊆ N_2(N_1(π^r P)) = N_3(π^r P), the SAME set for all case-(a) trees and for
  Σ^r(P) itself, and |N_3(π^r P)| ≤ 81|N_1(π^r P)| ≤ 81|Σ^r(P)| (COV, SH-1). Case (b): |π^r(Y_i)| ≤ 16 + 32ℓ_iL^{-r} (a tree of
  length λ is traversed by a closed walk of length 2λ, cut into ⌈2λ⌉ ≤ 2λ + 1 arcs of length ≤ 1, each inside a unit cube
  meeting ≤ 2⁴ boxes), ×625 by SH-2, summed: ≤ 10000r_i + 10000ℓ_i ≤ 40000ρ|Y_i|. ✓ So ‖P∪Y‖_sh ≤ 81‖P‖_sh + (1+40000ρ)|Y|.
- 81 < 2401 (the reviewer's lever) < 6561 (session 5). **Lever (a) is beaten as claimed.** COL′ (81(10002n + 10000M)) ✓.

*(F3 exact locations: SH-1 l.1825, SH-2 l.1832, Corollary H-geo′ l.1841, COV l.1855, SH-att′ l.1869, COL′ l.1943.)*

## F4 (T5) The ring price "×17 open / ×82 closed, and the closed column is what the proof uses" — **REFUTED** (the last clause, and with it PLD s7's reversal of HW §41 item 4 and HANDOFF's "settled"); ×17 **CONFIRMED as a valid bound**; ×82 a valid but loose bound; the needed ring is **free**
*Where:* HW l.1964 "Lemma RING (the price is ×17, not ×82)", l.2380 "Only the OPEN column enters #_{R′}"; PLD l.3054 "Finding
(BUF-CC)", l.3077 "Why this is not avoidable by using the level-k weight only", §19.10 "DOWNGRADE (cross-lane)", §19.11 item 1
to HW; HANDOFF "Two cross-lane disagreements" item 1 ("the closed column is the application the proof actually makes").
**(a) What the proof applies.** HW consumes (E2^𝔉′) in CRC-2T′ step (5) at j = m − 1 with Γ = 𝒟 (level m) and buys, in step (4),
R‴ := R′^{−(Col(Y) ∪ Col(N_1(col 𝒟 ∪ Y)))} — the OPEN column of the level-j set N_1(X), X := col 𝒟 ∪ Y. PLD's Corollary E2-RED
(l.2517) delivers (E2^𝔉′) from two inputs, and these are the only places a BUF is applied:
- **(D1)** (CEM^{COL})_{j+1} with A = Γ_0 ∪ Γ_1 under ν^w, **w = h^{R,1}_j**. For k := j + 1 this is a level-(k−1) weight — the
  generator for which BUF-CC is right that a CLOSED column at level k is needed: [N_1(Γ_0)] ∩ S_R = ∅ at level j + 1. But for a
  level-j cube z, "z R-free" means its open column {(j+1, π(z)), (j+2, π²(z)), …} misses S_R, and **π(N_1(col_j Γ)) = N_1(Γ)**
  (proof: for Q′ = Q + t, t ∈ {−1,0,1}⁴, take z′_i = 3Q_i − 1, 3Q_i, 3Q_i + 3 for t_i = −1, 0, +1; checked exactly on 200/200
  samples, r55h_geo G-C1). So the closed column of N_1(Γ_0) at level j + 1 **is the same set of pairs** as part of HW's open
  ring at level j. HW's ring supplies (D1)'s requirement.
- **(D2)** NA-PRICE^{E+} at level j for S = Y ⊔ x(Γ_1) ⊂ X under ν^w with w = h^{R,1}_j at level j (the level-k generator,
  k = j). Step (1) needs BUF at level j: N_1(S) R-free — supplied by HW's ring. Step (4) needs the marginal of ν′ on U_{≤j−1}
  not to read L^∂_{j−1}(S); **Lemma COL-DEC's first clause supplies that directly** (PLD l.2190ff (b); REVIEW_PLD_S5 S5-7
  re-derived it): the X_j(S) kernels integrate to 1 because neither 1_{R′,j} (GEO (iii): S declared, crossing links interior to
  no cube — true also for HW's non-product *-cluster constraint) nor w (BUF at level j) nor the buffer indicator reads them,
  and the surviving kernels c ∉ X_j(S) read U_{j−1} only inside their own endpoint blocks (GEO (i)). **No level-j pair (j, z),
  z ∈ N_1(S), needs to be unconstrained.** PLD l.3077 converts the level-k weight into h^{R″,1}_{k−1} (Lemma MARG — fine) and
  then certifies non-reading through Theorem LI^U-0′, which is only a SUFFICIENT condition; COL-DEC already certifies it.
**(b) Verdict.** Finding (BUF-CC)'s observation is right as stated about §18.7.0's class definition (a level-(k−1) generator
cannot be certified by the level-k hypothesis "N_1(𝒜) R-free") — **CONFIRMED**. Its consequence for HW ("the proof needs the
closed column, ×82; withdraw HW §41 item 4"; HANDOFF "§18.4's ×82 stands") is **REFUTED**: the closed column at level k that
(D1) needs is HW's open ring at level k − 1, and (D2) needs none. HW §41 item 4 stands.
**(c) The price itself (r55h_geo G-C2, G-C4; r55h_ring R1-R2).**
- HW Lemma RING's inequality |sh_{j+r}(N_1X)| ≤ 16|sh_{j+r}(X)| — **CONFIRMED** (N_1(Σ^r X) = N_1(N_1(A_r)) = N_2(A_r) = ∪ 2⁴
  translates; G-C4: 0 violations). As a PRICE it is valid but loose: the ring's pairs at level j + r are π^r(N_1 X), and
  π^r(N_1 X) ⊆ N_1(π^r X) ⊆ Σ^r(X) (iterate π(N_1 B) ⊆ N_1(π B), then SH-1; G-C2: 0 violations). So
  #(Col(N_1X)) ≤ Σ_{r≥1}|Σ^r X| ≤ ‖X‖_sh, and since Col(Y) ⊆ Col(N_1X) the merged relaxation of step (4) costs
  ≤ e^{c_U‖X‖_sh} — **exactly session 5's allowance for Col(Y) alone. The ring is free: c_+ = c_A + c_U**, and the honest (S2)
  ceiling with the ring is HW's "no ring" row, **1.52362·10⁻⁹⁴/c_+** (observed ratio of ring pairs to Σ_{r≥1}|Σ^r X| ≤ 0.035 on
  the samples, G-C3).
- PLD's ×82 (PLD §18.4; §19.1 "#_R([N_1X]) ≤ 81|X| + 16Σ_{r≥1}|sh_r(X)| ≤ 81‖X‖_sh") is a valid upper bound in HW's currency
  but loose even for the closed column: with the inclusion above, #([N_1X]) ≤ 81|X| + Σ_{r≥1}|Σ^r X| ≤ ‖X‖_sh + 80|X|, a
  PER-CUBE surcharge (b_n + 6480c_U, per-Y constant + 80c_U, b_D unchanged), giving 1.523470·10⁻⁹⁴/c_+ — ×81.98 above the ×82
  row (R2). So ×82 is wrong as a price under either reading.
- *A further defect of the closed-column purchase, unaddressed by PLD s7 and HANDOFF:* at m = k_0 + 1 it relaxes level-k_0
  pairs, outside CRC-2T′'s stated induction range ("every upward-closed set 𝒞′ of pairs at levels ≥ k_0 + 1"; HW §30.1 "All
  relaxations below are at levels ≥ k_0 + 1"). NOT-VERIFIED whether repairable; moot once (b) is accepted.
**(d) Downstream.** Every "g²_CRC at the ×82 ring" figure (HW l.2007 1.85835·10⁻⁹⁶; EPS1_SWEEP l.243/394/417; EPS1_EXEC
l.918) understates the HW-route (S2) ceiling by ×82. With HIST's constants as written the HW-route binding ceiling is HIST-sum
at **3.96620·10⁻⁹⁵/c_+** (c_f = 6561c_+), +1.33 decades over the ×82 (S2) figure; with H-geo′ adopted, 1.52354·10⁻⁹⁴/c_+ (A4).
Every such margin against DX′ only grows; **no NOT-BINDING verdict flips.** The citation slip (EPS1_SWEEP cites "HW l.2006",
the ×17 row, for 1.85835·10⁻⁹⁶, which is l.2007) — **CONFIRMED** (awk of HW l.2000-2010).

*(F4 (D2) relies on PLD l.1766 Lemma COL-DEC as written in session 5: "G′ := Φ_{k-1}·H′ … does not read U_{k-1} on L^∂_{k-1}(S)",
whose proof keeps 1_{R,k-1} whole — it never factorises the constraint. Re-read and re-derived here; agrees with REVIEW_PLD_S5 S5-7.)*

## F5 (T4) The HW/PLD interface defect and its repair by "Proposition PATCH"
*Where:* PLD l.2347ff §18.6 (Proposition PATCH (i)-(v)); HW §37 l.2095-2101 ("Theorem NA-PRICE^E/E+ generate no allowance at all,
they only TRANSMIT …"), (E2^𝔉′) l.2103-2117; PLD l.2517 Corollary E2-RED.
- **(i) The defect exists — CONFIRMED.** Session 5's (E2^𝔉) asked a union-form allowance over the attached patch; PLD §17 delivered
  the slice s_k(𝔥) (PLD l.1848/1856) or ‖S‖_sh (l.1408). PATCH (ii)'s incomparability is right in both directions (s_k(𝔥) = 0
  for a history with components only at level k + 1 while ‖S‖_sh ≥ 1; a deep history makes s_k large with |S| = 1).
  "Found independently from both sides": the CURRENCY defect was found independently by REVIEW_HW_S5 (S5-16 (1)) and
  REVIEW_PLD_S5 (S5-9/S5-10/B2). PATCH itself is not an independent third finding — PLD §18.6's "Record" says it was written
  after REVIEW_HW_S5's essentials were relayed.
- **(ii) The diagnosis "NA-PRICE generates no allowance, it only transmits the hypothesis's" — CONFIRMED for NA-PRICE^{E+},
  REFUTED for NA-PRICE^E (i).** For E+ (PLD §18.7.1): law conversion exact (BUF + FT^far: no allowance), KD and CW pointwise, the
  moment (CEM^{COL}) per-cube (c_cem^{|S∖T|}) — so c_A = 0 out, as stated. For E (i) (§17.4, which uses Lemma MD), PATCH (iv)
  (PLD l.2384) rests on "(by §18.5 (b′)) a per-cube depth-free Δ_sh" — **false** (F9): MD's push-down to x(S) changes the
  allowance by ‖x(S)‖_sh − ‖S‖_sh, which grows by 175 per level per cube at the position of F9 and is bounded only
  multiplicatively (‖x(S)‖_sh ≤ 16‖S‖_sh + 81|S|). So "NA-PRICE^E … transmits unchanged" (HW l.2099-2100, PATCH (iv)) is
  wrong for E (i). HW's route uses E+ only (via E2-RED), so the consequence for HW is nil; the sentence should say "E+".
- **(iii) Do the two repairs match? — CONFIRMED as of session 6 (hypothesis, allowance, level range all identical); but the
  matched statement is FALSE as quantified (F6), and PLD session 7 asked HW to break the match (F4).** HW §37 (E2^𝔉′) and PLD
  E2-RED agree on: the ring hypothesis "N_1(col(Γ) ∪ Y) R-free" (open column at level j); Γ ∩ A_{j+1}(𝔥) = ∅ or Γ = 𝒰_{j+1};
  F_< universally quantified; buffered weight; allowance read as (P0)/(P1) with the patch form by monotonicity (PATCH (i), which
  is right: Y ⊔ x(Γ_1) ⊂ col_j(Γ) ∪ Y and ‖·‖_sh is monotone); c_A = 0 delivered. Two defects in the match:
  (a) **both carry the universally quantified F_<**, which makes (E2^𝔉′) false (F6); (b) **level coverage at j = k_0**: HW asks
  "every level j ≥ max{k_0, 1}", while E2-RED's (D2) step needs NA-PRICE^{E+} at level j inside 𝔏^buf_j, whose F_< must read
  levels ≤ j − 2 (PLD l.2446 "k_0 ≤ k − 1"); with F_< of U_{<k_0} and j = k_0 that fails. So E2-RED delivers j ≥ max{k_0 + 1, 1}
  as stated. (With F_< restricted to the specific spectators Π_{k′<j}Φ_{k′}, GEO (iv) handles Φ_{j−1} and j = k_0 is
  recovered — another reason for the restriction of F6.) HW has no session 7, so PLD §19.11's request (closed ring, ×82) is
  unanswered; per F4 it should be declined.

## F6 (new) The universally quantified F_< — PLD §18.6.2 Delta 3 / M-7, 𝔏^buf_k step 1, (CEM^{COL}), Cor. E2-RED, HW §37 bullet 5, HW §38 item 5 — **REFUTED**
*Where:* PLD l.2415 "Delta 3 (F_< is a free unquantified symbol) — FREE on PLD's side … (E2^𝔉) may be quantified 'for every
bounded measurable F_< ≥ 0 of U_{<k_0}' at zero cost"; PLD l.2446 "with any bounded measurable F_< ≥ 0 of U_{<k_0} inserted";
PLD l.2461-2462 (CEM^{COL}) "c_cem < ∞, independent of g ≤ g_0, k, K, T, 𝔥, R, 𝒜, A, A′, F and F_<"; PLD l.2520; HW l.2111
"every bounded measurable F_< ≥ 0 … (universally quantified; free on node A's side …)"; HW l.2186 (§38 item 5).
- *Why "free" does not follow.* Delta 3's argument is that F_< does not READ the links FT^far/COL-DEC are about. That is a
  statement about the law conversion (and it is true: FT^far and COL-DEC hold for any F_<). It says nothing about whether the
  BOUND survives: F_< enters the law ν^{R,F}_j as a density factor and can condition the finer fields on any event of positive
  probability, which then drives the coarse fields through the kernel chain.
- *Counterexample to (E2^𝔉′) as stated.* Γ = ∅, Y = {y}, R := R(𝔥)^{−Col(N_1 Y)} ∈ 𝔉_𝔥 (so N_1(Y) is R-free),
  F_< := 1_E with E := {U_{k_0−1} within δ, under y's blocks, of a coherent configuration whose block-averaged level-j kernel
  centres give an interior plaquette of y holonomy distance ≥ 2ε_1}. The kernels concentrate at their centres with
  fluctuations O((κu)^{−1/2}) → 0 and coherent curvature scales by L² per level upward (PLD §18.5 (e), "p5 B3, exact"), so under
  ν^{R,F}_j, y ∈ D_j with probability → 1; w = h^{R,1}_j does not read y's links (y and N_1(y) R-free, Theorem LI^U-0′), so
  ν^w(y ∈ D_j, Buf good) → ν^w(Buf good), which is not small, while the bound is C_Ae^{−a_Au_j} → 0. (E2^𝔉′) fails.
- *Counterexample to (CEM^{COL})_k as stated (same mechanism, more directly).* F_< may read U_{k−2} on Q's own column. Take
  F_< = indicator that U_{k−2}|_{col_{k−2}Q} is near a coherent configuration making Q ∈ 𝒞_k(U_{k−1}) likely; then by Lemma CW
  (or directly: F^col_Q(U_{k−1}) ≥ c(δ) > 0 g-independently for a coherently curved U_{k−1}, since a zero-energy finer completion
  would have to be flat), E_ν[e^{θY^f_Q}] ≥ e^{24θu_kc(δ)} — no g-uniform c_cem. **This is exactly PLD's own §18.7.2 (α)
  argument against the "any w" form, with the weight replaced by F_<** — and F_< has more access than w (it may read the column).
- *Who was right.* REVIEW_HW_S5 S5-16 (3) and its binding fix [RHW5-fix E2-2] said: "name the class of F_< (the capped product
  Π_{k′<j}Φ_{k′}, not an arbitrary bounded weight)" — **CONFIRMED and sharpened here to explicit counterexamples.** HW s6 reversed
  that fix while recording it as applied (F17). The repair: quantify F_< over the specific history spectators (PLD §17.2's law,
  PLD l.1736, already carries them), or over bounded F_< measurable off region(A). Everything downstream that quantifies over
  all F_< — (CEM^{COL}), Proposition ONE's input, (ACT′), (LCR^act′), (EQ-bc)/(BCH-1) as stated — inherits the defect: as
  quantified they are false, and the implications from them are vacuous until restated.

## F7 (T15) HW §35.7's constants, ratios and ledger (l.1995-2045) — table **CONFIRMED**; two printed figures **REFUTED (immaterial)**; §35.7 (i)'s attribution **REFUTED**
- **Table (A1, PASS):** all 15 integers b_n, b_D, c_f equal the printed values exactly, and all 10 rigorous enclosures of
  g²_CRC and n_T round to the printed 6-figure values (e.g. s6 ×17: 8.963761520e-96, 5.458401229e95).
- **S5-12 coincidence (A2, PASS):** (S2) 4.897893908e-97, REL-boot 4.898021401e-97, HIST-sum 4.898012184e-97, n_T 9.991038207e96 —
  every printed version (review's 5-6 figures, HW's 7) is the correct rounding.
- **Ratios (A3):** 204.17, 11.16, 53.81, 1.52, 1.96e55, 1.9592e55, 3.5855e56, 6.0954e57, 2.88112e-98, 1.83822e-93, 3.67644e-98,
  2.33375e-96, 42.85, n_H/n_T = 3.84 all reproduce. Two do not:
  - "÷311.2 on n_♯" "at every ring value" (l.2008): at c_+ = 1 the exact n_T ratio is **311.1228** (rounds to 311.1); 311.17 at
    ×17 and ×82. Immaterial. **REFUTED as printed.**
  - "n_H = 2.09688·10⁹⁶" at the ×17 ring (l.2025): with the B_0 = c_f + 2 that the same paragraph states, n_H = **2.096918·10⁹⁶**;
    2.09688 is the value at B_0 = c_f. The same B_0 slip sits in REVIEW_HW_S5's S5-12 table ("n_H(a, B_0) … B_0 = 531441c_+",
    9.99102e96, against "B_0 = 531441c_+ + 2" in the HIST-sum row): at B_0 = c_f + 2, n_H = 9.991057e96 > n_T = 9.991038e96, which
    makes "(T) imposes nothing beyond n_♯ ≥ n_H" hold strictly. Immaterial. **REFUTED as printed (convention slip).**
- **§35.7 (i) "the breach against 10⁻⁹⁴ … does NOT disappear. Two independent reasons … node A's buffer ring costs ×17 on top"
  (l.2017-2019) — REFUTED as attributed.** By F4 the ring costs nothing, so (S2) at the ring is 1.52362·10⁻⁹⁴ — ABOVE 10⁻⁹⁴ by
  ×1.52 (+0.18 decades, R4). What still sits below 10⁻⁹⁴ is HIST-sum with HIST's unsharpened 38417 (3.96620·10⁻⁹⁵, ×2.52 below,
  −0.40 decades): the residual breach is §35.7 (ii)'s failure mode (W-F3), not the ring and not SH-neg. Non-decisive, since
  10⁻⁹⁴ is not the binding ceiling (F1).
- **§35.7 (iii) "(S2) costs the programme nothing … ≈ 56 orders of slack" — CONFIRMED** (F1; 55.3-57.8 decades in every
  convention).

## F8 (T6) PLD s6 "(E2^𝔉)'s law conversion closed and priced" — **CONFIRMED** (closed for HW's application under the open ring); "priced at ×82" a valid but loose bound (F4)
*Where:* PLD §18.2 (l.2106ff), §18.4 (l.2188ff), §18.11 "UPGRADE. The far-set class and the push-down for HW's weight … are supplied".
- (C_S′) audit: GEO (i), (iii), (iv), FT^far, COL-DEC use only S ∩ 𝒰_k = ∅ — CONFIRMED by reading the four proofs (PLD l.1745-1772).
- Lemma FT^far′ (hypothesis L_G ∩ ℓ(S) = ∅ suffices): Step 2 integrates only ℓ(S) and the factors reading U_k there are the
  kernels, 1_{R′,k} (GEO (iii)), the spectators (levels < k) and G — CONFIRMED (and REVIEW_PLD_S5 S5-6 found the same gap).
- Proposition FAR (i)-(ii): y ∈ 𝒰_j ⇒ π^{m−j}(y) ∈ A_m(𝔥) for all m > j by 𝒰_j ⊂ Ω^c_j, π(X) ⊂ Σ(X) and H-nest (i), so a
  non-R-free cube is not in 𝒰_j; and a history child would put π(x) ∈ A_{j+1}(𝔥) — CONFIRMED. CRC-2T's animals satisfy
  Γ ∩ A_{j+1}(𝔥) = ∅ because they lie in S_{R_t} ⊂ S(𝔥) = complement of A(𝔥) — CONFIRMED.
- Lemma BUF (N_1(𝒜) R-free ⇒ L_w ∩ X_j(𝒜) = ∅): a link with an endpoint in a cube of 𝒜 has both endpoint cubes in N_1(𝒜) —
  CONFIRMED.
- Session 7's Finding (BUF-CC) does not reopen this for HW: (D1) needs exactly HW's open ring, (D2) needs only level-j BUF +
  COL-DEC (F4 (a)). The class-definition slip in §18.7.0 (level-(k−1) generators certified by a level-k hypothesis) is real and
  is fixed by stating each generator's ring at its own level.
- Price: PLD's ×82 = 1 + 81 is a valid upper bound; HW's ×17 tighter; the true marginal cost is ×1 (F4 (c)).

## F9 (new) PLD §18.5 (b′) "‖x(S)‖_sh ≤ ‖S‖_sh + (1 + Δ_sh)·|S|, Δ_sh = 3073361, depth-free" — **REFUTED** (and the claims resting on it)
*Where:* PLD l.2266-2276 ("(b′) The allowance does NOT compound … PROVEN-HERE"); l.2783 ("Compounding is NOT a reason: §18.5 (b′)
PROVES …"); l.2834 ("UPGRADE. The union-form excess line review B2 (b) left open is PROVEN"); l.2384 (PATCH (iv)'s Δ_sh clause);
source of Δ_sh: §16.6 (b) l.1460 and §16.7 l.1491-1493 ("the excess is additive and depth-free, p4 D2b").
- *The mechanism of HW's own Proposition SH-neg, one level down.* Take Q = (q,q,q,q) at level k with q = 3w, w = (3^D − 1)/2 (all
  base-3 digits 1), S = {Q}, x_Q = (3q, …) any child. In 1D: Σ^r(q) = {w_r − 1, w_r, w_r + 1} for r ≥ 1 (a 3-set for ever, since
  w_r ≡ 1 mod 3), while Σ(x_Q) = N_1(Q) and Σ(N_1 q) = N_1({w_1 − 1, w_1}) is a 4-set that stays a 4-set ({w_r − 2, …, w_r + 1}
  projects to {w_{r+1} − 1, w_{r+1}}). In 4D the per-level excess is 4⁴ − 3⁴ = **175 for every level**.
- *Exact check (r55h_geo G-B, pre-registered REFUTED-iff):* direct 4D = product for D = 2..7; the excess ‖x(S)‖_sh − ‖S‖_sh is
  81 + 175D exactly (431 at D = 2, 10581 at D = 60; increments exactly 175 on D = 10..59) and **3500081 > 1 + Δ_sh = 3073362 at
  D = 20000**. Control G-B3 (q = w itself): excess 81 at every depth, so the growth is the position, not the code.
- *Correct statement.* Σ^r(N_1 S) ⊆ N_1(Σ^r S) and |N_1(Σ^r S)| ≤ 16|Σ^r S| (HW's Lemma RING step), so
  **‖x(S)‖_sh ≤ 16‖S‖_sh + 81|S|** — multiplicative, not additive; and the multiplicative constant cannot be below 256/81 (the
  family's ratio (82 + 256D)/(1 + 81D) → 256/81).
- *What falls.* (b′) (PROVEN-HERE) is false; "Cor. LAW (c) is correct in the union currency" and "compounding is NOT the
  obstruction" are false — a recursion through x(S) multiplies the allowance constant by up to ≥ 256/81 per level, i.e.
  compounds geometrically; §18.11's UPGRADE is a downgrade; PATCH (iv)'s Δ_sh clause is false (F5 (ii)). §18.5's verdict
  (NP-F6: the level induction does not close) survives, with one more reason. Upstream (session 4, outside this batch, flagged):
  §16.6 (b)'s "depth-free" excess and §16.7's c_sf := e^{2c_U(81 + Δ_sh)}c_lcr ([RPLD4-fix C-1]) are not valid as per-cube constants.
  REVIEW_PLD_S5 S5-9 (b) ("plausible (the deep shadows of x(S) and S coincide)") and its binding fix B2's second clause
  (asking for this line) asked for a false statement (F20).

## F10 (T7) PLD s7 "(CEM-2) dissolved" — **REFUTED**
*Where:* PLD l.3043 Lemma READ (iii) "1_{R,k-1} factorises per level-(k−1) cube, each factor 1{ζ_x = 0} …"; l.3096 Lemma DLR (i)(β)
"the constraint factors Π_{x∈col_{k-1}(S)∩S^{(k-1)}_{R′}}1{ζ_x = 0}"; DLR (iii); l.3118 Theorem W-FREE (a)-(b); l.3340 Theorem OUT,
(EQ-bc) l.3350; l.3365 "Status of (CEM-2)"; §19.8 "(CEM-2) does not appear: Theorem W-FREE removes it"; §19.10 UPGRADE "(CEM-2) → not
needed".
- **(a) The factor audit is wrong.** The pattern indicator is HW §13.1 l.614: **R_{S,E} := ∩_j{every *-component of
  (D_j ∪ E^{(j)}) ∩ S^{(j)} has ≤ n_♯ cubes}**, with n_♯ ≥ n_H ≈ 10⁹⁵ — defects ARE allowed in clusters up to n_♯ (CRC-2T step (2)
  prices exactly the (n_♯ + 1)-animals). 1_{R,k−1} is a function of the defect indicators, but NOT a product of 1{ζ_x = 0}.
  (PLD's own session-5 COL-DEC, l.1766-1772, correctly keeps "1_{R,k-1}(U_{k-1})" whole.) So READ (iii) is false, and with it
  DLR (i)(β) and (iii): given 𝔊, the conditional law of U_{k−1}|_𝔏 carries the indicator that adding col(S)'s defects to the
  𝔊-measurable OUTSIDE defect configuration creates no *-component > n_♯. Example: an outside *-cluster of exactly n_♯ level-(k−1)
  defects touching a cube x of col_{k−1}(S) forces x good; remove the cluster and x may be a defect. P_S therefore depends on 𝔊
  beyond U_{k−2}|_{region(S)}, and does not factorise over Q ∈ S (clusters can join adjacent columns).
- **(b) The weight is not eliminated.** The outside clusters run through the ring (whose level-(k−1) constraints (RING-cc) does not
  touch) into the non-R-free region that w = h^{R,1} reads; so w and ζ = E_{ν_0}[Z | 𝔊] are correlated. W-FREE (a) ("the far weight
  h^{R,1} does not appear in ζ at all … the separation across the R-free ring is a Markov statement, exact, with cost 1") and
  (b) ("what survives of (CEM-2) is only the ν^w-law of U_{k-2}|_{region(S)}") are **false**. What survives of W-FREE is the trivial
  tower identity E_ν[ZF] = E_ν[ζF] for ANY σ-field making wF measurable — true and contentless.
- **(c) The replacement residual is not smaller.** Theorem OUT's identity is valid (tower property, wF 𝔉_out-measurable), but
  (EQ-bc) as stated — "there are B_0 < ∞ and an 𝔉_out-measurable charge 𝔟_Q ≥ 0 such that E_λ[𝔞^col_Q | 𝔉_out] ≤ B_0 + 𝔟_Q" — is
  **vacuous**: 𝔟_Q := sup_{λ∈[0,λ_f]}E_λ[𝔞^col_Q | 𝔉_out] (bounded, measurable) and B_0 = 0 satisfy it. So (EQ-bc) + (BCH-1) is
  (ACT′) restated up to a sup/expectation exchange; PLD l.3361-3364 itself says the charge's definition "is not done here".
  "(BCH-1) is strictly smaller than (CEM-2), in four named ways" is a ranking by form, not a proven implication either way.
- **(d)** With F_< universal (F6), (ACT′)/(BCH-1) as quantified are false anyway.
- **Correct status:** (CEM^{COL}) ⇐ (ACT′) (Lemma DOM′ + the exponential-family identity: valid). No residual smaller than a
  weighted-law decoupling has been isolated; (CEM-2)'s screening content is not removed, it is relocated into (ACT′)/(BCH-1)
  under the same weighted law. §18.11's "single biggest remaining obstruction = (CEM-2)" is not superseded in substance.

## F11 (T8) PLD s7 "(LCR) restated past its own impossibility" — **REFUTED** (as argued)
*Where:* PLD §19.4 clause 2 (l.3237-3238: "§18.8 (i)'s fatal objection … does not apply to a **first moment** of 𝔄^col"),
l.3246-3247, §19.5 "(LCR^act′)", §19.10 T19 (c) (l.3547-3549).
- By §19.5's own identity, log E_{ν^G}[e^{λ_f𝔞^col_S}] = ∫_0^{λ_f}E_{λ,G}[𝔞^col_S]dλ, so a uniform bound on the λ-tilted FIRST
  moments for λ ∈ [0, λ_f] is EQUIVALENT (on average in λ) to the exponential-moment bound (log c_act = λ_fB). And §18.7.2 (α)'s
  mechanism — a weight forcing column curvature of order ε_1 — bounds the tilted first moment below by ≈ u·c(ε_1) → ∞ just as
  it bounds the exponential moment. "It is a first moment, not an exponential one" therefore does not escape §18.8 (i).
- What actually separates (LCR^act′) from §16.7's (LCR) is the restriction to buffered weights — already present in
  (CEM^{COL}) — and clause 2's "demotion" of that restriction rests on Lemma DLR, which is false (F10).
- (LCR^act′) quantifies "every bounded measurable F_< ≥ 0 of U_{<k_0}": false as stated (F6).
- Clause 5 "B ≤ 10⁹/λ_f" inherits §18.8 (ii)(5)'s stale side condition (F14).
So (LCR^act′) is a well-posed OPEN statement once F_< is restricted, but it is not "past its own impossibility" for the reason given.

*(Locator correction for F10 (c): the "What the charge must be" paragraph is PLD l.3358-3363; "Supplying that definition … is not
done here" is l.3362.)*

## F12 PLD session 7, the remaining PROVEN-HERE / counted items ([E7] (1)-(3))
- **Lemma READ (i), (ii), (iv), (v), (vi): CONFIRMED** (read-sets; (v) needs k_0 ≤ k − 1, which is exactly the j = k_0 gap of
  F5 (iii)(b)). **READ (iii): REFUTED** (F10 (a)).
- **Finding (BUF-CC): observation CONFIRMED, consequence REFUTED** (F4). **Lemma MARG: CONFIRMED** (Fubini + HW Lemma TILT (i):
  integrating U_k against K_{k-1}·1_{R′,k} turns h^{R,1}_k into a level-(k−1) future weight).
- **Lemma DLR: REFUTED** in (i)(β) and (iii); (iv)'s identity is the tower property and holds for any 𝔊 making wF measurable.
  **Theorem W-FREE: REFUTED** in (a)-(b) (F10 (b)).
- **Lemma DOM: CONFIRMED with a constant slip.** F^col_Q is an infimum, so it is ≤ the column sum at the actual fields ✓; the
  ratio u_k/u_i ≤ 1/(1 − Rg_k²) ✓; but the last step uses "g_k ≤ g_K for k ≤ K, (F_R)", whereas (F_R) gives only
  g_k² ≤ g_K²/(1 − Rg_K²) (RLARGE l.832 says so), so the bound is 1 + 4Rg_K² (for Rg_K² ≤ ½), i.e. λ_f should read
  24θ(1 + 4Rg_K²) — immaterial at Rg_K² ≲ 10⁻⁹⁴R, and the same slip is in §16.7's proof. **Lemma DOM′, Theorem AT:
  CONFIRMED** (AT is the standard identity for the exponential family generated by a bounded statistic).
- **(ACT) withdrawn (§19.5): CONFIRMED as a withdrawal** (the extensivity argument is ARGUED, as labelled; withdrawing a
  hypothesis needs no proof). **Proposition ACT-EQ (i)-(ii): CONFIRMED; (iii) "strictly stronger": NOT-VERIFIED** (a structural
  remark, not a proof of non-implication).
- **Proposition TRADE (ii)** (layer-cake: ν(𝔟 > t) ≤ Ce^{-t} ⇒ E[e^{λ𝔟}] ≤ 1 + Cλ/(1 − λ)): **CONFIRMED.** (i)'s numbers are
  evaluated at the stale g_K² = 10⁻⁹⁴ (F15).
- **Theorem OUT: CONFIRMED as an identity; its "reduction" is vacuous as stated** (F10 (c)).
- **Theorem L0:** dimension count CONFIRMED (216 interior links of a 3⁴ block, 648 real dimensions, one all-interior site, 645
  transverse); log C_fc^{(0)} = (645/2)·ln(24/23) = 13.7255 CONFIRMED (recomputed). **(ii) REFUTED as stated**: "the conditional
  law of U_0|_{int Q} given 𝔉_out is the Wilson measure … times the factor 1{ζ_Q = 0} if Q ∈ S^{(0)}_R" (l.3424) repeats READ
  (iii)'s error — the level-0 constraint is the n_♯-cluster indicator, coupling the cubes of Γ to each other and to outside
  defects; the per-Q statement (W0-EQ) is therefore not what the conditional law delivers for *-adjacent Γ.
  **"(0a) is the weaker, and strictly. PROVEN-HERE" (l.3405): NOT-VERIFIED** — (0a) (Γ at level 0, Wilson window, Y = ∅) and (0b)
  (Γ at level 1, Y at level 0) are different statements, neither implying the other as written; the argument ranks known
  routes. **§19.11 item 2 to HW ("state (E2^𝔉′)'s level-0 clause as (0a) only, and drop (0b)", l.3660): REFUTED as a
  recommendation** — CRC-2T′ step (5) at j = m − 1 = 0 (animals 𝒟 at level 1, far defects Y at level 0; needed for (CRC)_0 /
  Cor. CRC-HW at k = 0, which TEL-f uses) is exactly (0b)-shaped, so (0b) cannot be dropped without leaving that step
  unsupported. **"(NP-F13) is REFUTED" (§19.7): NOT-VERIFIED** (it rests on L0 (ii)).
- **Route (ρ2) (ARGUED in file): NOT-VERIFIED here**; its price (1) "×82 instead of ×17" should read ×1 (F4).
- Net for the session-7 tally (+3 counted): [E7] (1) does not stand as PROVEN (READ (iii), DLR, W-FREE refuted; BUF-CC's
  consequence refuted); [E7] (2) stands only as the identities (DOM′, AT, ACT-EQ (i)-(ii), OUT) — the (LCR^act′) restatement it
  bundles is not past the impossibility (F11); [E7] (3) stands for the dimension count and the window constant, not for (ii).

## F13 PLD session 6, the remaining items ([E6] (1)-(2) and the uncounted ones)
- **[E6] (1)**: (C_S′), FT^far′, FAR, BUF — CONFIRMED (F8); PATCH (i)-(iii), (v) — CONFIRMED; PATCH (iv) — CONFIRMED for E+,
  REFUTED for E (i) (F5 (ii)).
- **[E6] (2)**: Theorem NA-PRICE^{E+} (i) — CONFIRMED as an implication (the 2^{|S|} split by T; FT^far after BUF; KD on T;
  CW on S∖T; (CEM^{COL}) on the COL-DEC marginal; the F′-measurability check of step (4) holds because the 1{Q ∉ 𝒞_k}, Q ∈ T,
  read only blocks under T). Corollary E2-RED — CONFIRMED as an implication for j ≥ max{k_0 + 1, 1} (F5 (iii)(b)).
  Proposition ONE (a)-(d) — CONFIRMED as logic (pointwise 1{Q ∈ 𝒞_k} ≤ e^{θY^f_Q}e^{−6θa_badu_k} by CW gives (J-NS^cd) with
  a_cd = 6θa_bad). "Strictly stronger" disclosure — fair. Proposition SPLIT — CONFIRMED as logic. **But the single hypothesis
  (CEM^{COL}) is FALSE as quantified (F6)**, so every "⇐ (CEM^{COL})" in §18.7 is vacuous until F_< is restricted.
- **§18.5 Proposition CHAIN**: the verdict (NP-F6) — CONFIRMED (no base case; nested certificates); (b′) — REFUTED (F9);
  (e) ARGUED as labelled; (f) the (EG-cur) disjunction — CONFIRMED as logic (kernel-energy grading is zero at a centre defect).
- **§18.7.2 (α)/(β)** "the buffer-good EVENT cannot supply a g-independent constant": CONFIRMED qualitatively (ε_1 is g-free,
  g_K → 0). The number is stale (F15).
- **§18.9 M-1 … M-7**: CONFIRMED as a comparison table, except M-7 ("free") — REFUTED (F6).
- **§18.10 check p6**: the F2 FAIL is honestly disclosed; but "§18.5 (b′)'s proof does not use the numerical value of Δ_sh, only
  that it is finite and depth-free, which §16.6 (b) and p4 D2b supply" — the depth-freeness is false (F9) and p4 D2b sampled
  random positions, the same blind spot as HW's B2 (REVIEW_HW_S5 S5-24).

## F14 PLD §18.8 "the c_lcr verdict" — value-not-load-bearing **CONFIRMED in substance**; its quantitative side condition **REFUTED (stale)**
*Where:* PLD l.2633ff ("In every one of these, c_lcr enters only through log c_lcr, additively, against b_n ≈ 2.04·10¹⁰·c_+"),
l.2660 (clause (5) "log c_lcr ≤ 10⁹ (so HW's (S1)/(S2) ceilings move by < 5%)"); §19.4 clause 5 / §19.5 "B ≤ 10⁹/λ_f".
- p6 B3's 1.0490 at session 5's b_n reproduces (r55h_arith A7). But (i) in (S1) log C_A enters against c_+c_att(ρ) + log(2Δ_ρ²),
  not against b_n: at session 5 (c_att = 1229313) log c_lcr = 10⁹ moves (S1)'s ceiling by **×814**; (ii) at HW session 6's
  constants (written concurrently, ÷311 on b_n) the (S2) factor at log c_lcr = 10⁹ is **×16.24** (open ring = the ring the proof
  needs, F4), ×1.90 (×17), ×1.19 (×82); (S1)'s is ×3126 / ×185 / ×39 (A7 records). So "< 5%" is false; the <5% threshold at the
  current constants is log c_lcr ≲ 3.3·10⁶ for (S2). The qualitative verdict survives: the equipartition-size value log c ≈ 1.8·10⁴
  moves (S2) by 3·10⁻⁴, and any finite c_lcr shifts g-independent ceilings only. §18.8 (iii) ("no PROVEN statement rests on the
  uncertified value") — CONFIRMED.

## F15 The "4.489·10¹⁵" gap (PLD §18.7.2 (α)/(β) l.2595; p6 A2; §19.6 (i) "2.2445·10⁶ in the log"; HANDOFF critical path item 3) — arithmetic **CONFIRMED**, currency **stale**
u·ε_1² = ε_1²/g_K² = 4.489·10¹⁵ exactly at g_K² = 10⁻⁹⁴, ε_1 = 6.7·10⁻⁴⁰ (A8). But 10⁻⁹⁴ is the (RLF-δ) "recorded" ceiling, which
the HW route itself sits below and which is not the programme's coupling: at the HW-route ×82 binding value 4.838·10⁻⁹⁷ the gap is
9.28·10¹⁷, at the DX′ ceiling 2.5·10⁻¹⁵² it is **1.80·10⁷³** (A8 records). The direction of every conclusion drawn from it
(the event route cannot work) only strengthens; the specific "misses the ceiling by 2.2445·10⁶ in the log" (§19.6 (i)) should
be quoted as "≥ 10⁶³ in the log at the binding coupling".

## F16 (T9) SYMBOLS.md SYM-F1 #1: "PLD l.1098 m_τ = 3 is wrong; 66/90/122 at RLARGE's threshold" — **CONFIRMED** (arithmetic and mislabel), with three scope corrections
*Where:* PLD l.1096 "RLARGE's η_1 = c_1ε_1 (c_1 = 1/117 < 2/L² = 2/9)", l.1097-1098 "(L²/(2C_I))^{m}c_1 ≥ 2C_IL^{-2}, i.e. m_τ = 3 at
L = 3 if C_I = 1", l.1100 "(PLD)_k at RLARGE's thresholds is an output of steps k, …, k + m_τ"; repeated l.1206, l.1244 ("m_τ = 3, 4,
5"), l.1260 (all four verified by sed); RLARGE l.64 "η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))}", A_d(3) = 9 (RLARGE l.973).
- *Arithmetic (r55h_arith A5, exact):* least m with (9/(2C_I))^m·η_1 ≥ 2C_Iε_1/9 is (3, 4, 5) for η_1 = ε_1/117 (any ε_1) and
  **(66, 90, 122)** for RLARGE's η_1 at ε_1 = 6.7·10⁻⁴⁰, N = 2 (quadratic branch active: ε_1 < 256N). Control at ε_1 = 2 gives
  (5, 7, 10), REVIEW_PLD_S3 l.435's recorded values. The diagnosis (l.1097 substitutes c_1 = η_1/ε_1, which is constant only for
  the linear η_1) is right: PLD l.1096 asserts "RLARGE's η_1 = c_1ε_1", and RLARGE.md (not edited in sessions 24-25) still
  defines the quadratic η_1.
- *Scope corrections.* (1) ε_1 = 6.7·10⁻⁴⁰ is a ceiling, not a value (RLARGE l.71-73); m_τ grows like log(1/ε_1), so the honest
  statement is "m_τ ≥ 66 (C_I = 1) at every admissible ε_1", not "66" (agree with Codex SYMBOLS F1). (2) "LIVE DEFECT" overstates
  its liveness: m_τ is the look-ahead depth of the PLD-desc architecture that REVIEW_PLD_S3 Arch-1/2/3 declared WRONG and that
  PLD §18.0's read list confirms is "not rebuilt on here"; no current statement consumes it (grep: only PLD §15, PROOF l.93, and
  review/audit files mention m_τ). (3) PROOF.md l.93 records that if the owner adopts KN-step's linear η_1, "m_τ becomes
  ε_1-independent at 3/4/5" — so l.1098 is wrong against today's RLARGE and would become right under that pending decision.

## F17 HW session 6, the remaining items
- **§38 "All eleven are applied; none is declined" (l.2178) — REFUTED for [RHW5-fix E2-2].** The fix (REVIEW_HW_S5 (a) item 5)
  said "name the class of F_< (the capped product Π_{k′<j}Φ_{k′}, not an arbitrary bounded weight)"; §38 item 5 (l.2186) records
  "F_< universally quantified over bounded measurable functions of U_{<k_0}" — the opposite, and false (F6). The other ten are
  applied as described (spot-checked against the S5 fix list).
- **§38 item 6 / §37 TF-2: siding with node A against REVIEW_HW_S5 S5-19 — CONFIRMED.** S5-19's premise "no node-A statement is
  written under such laws" is contradicted by PLD l.1736: "ν^{(k)}_k … density ∝ e^{-S_0}Π_{i<k}K_iΠ_{j≤k}1_{R(𝔥),j}Π_{k'<k}Φ_{k'}".
- **Theorem CRC-2T′ (§36, l.2063ff): CONFIRMED** for its four session-6 replacements (SH-att′, COL′, R‴ with the ring, the
  constants; F3, F4) — with F4's note that the needed ring costs nothing. The session-5 body: spot-checked steps (1)-(6)
  (telescoping exact; step (2)'s component argument; step (4)'s event inclusion {Y(c) = Y} ⊂ E_Y; the collar sum with
  162·17⁴/Δ_ρ² ≤ 1.94·10⁻³), agreeing with REVIEW_HW_S5 S5-8 … S5-10; not re-proved line by line. Its hypothesis (E2^𝔉′) is false
  as quantified (F6) until F_< is restricted — the implication is then vacuous, not wrong.
- **§35.6 (c) "nothing else in CRC-2T reads R″" — CONFIRMED** (Y(c) is fixed relative to R′; Buf^{R‴} ⊆ Buf^{R″}; step (5)'s peel
  only gains; the induction hypothesis at R′ with N(R′) < N(R)).
- **§36 "V2 (a) NOT DELIVERED", gas framing dropped — CONFIRMED** (no partition function, compatibility relation, Mayer identity
  or KP criterion anywhere in §30/§36).
- **§37 level clause: CONFIRMED** that HW l.1530's clause is mis-levelled and that neither reading is delivered; see F12 for why
  both (0a) and (0b) shapes are consumed.
- **§37's narrowing of §24.3's doubt (REVIEW_HW_S5 S5-17) — NOT-VERIFIED** (an expectation-vs-pointwise argument, ARGUED; plausible).
- **§41 items 1-3 — CONFIRMED** (HANDOFF's "lower g_0" withdrawn, F1; H-geo′ request to HIST is a strict sharpening; RLARGE row
  10g relabel). **§41 item 4 (ring ×17) — CONFIRMED against PLD session 7** (F4), and sharper than HW claimed (×1).
- **§39 check w6:** G1-G6, A1-A6, N1-N2 as recorded — G-A/A1/A2 reproduced independently here; the w6 criteria hash
  060c5322… matches HW_LOG; G5's self-disclosed defect is correctly reported as uninformative.

## F18 (T10) SYMBOLS.md SYM-F1 #2: "HW l.604 a_bad ≈ 5e-23/C_D⁴ should be ≈ 5.01e-22/C_D⁴ (×9)" — coefficient **CONFIRMED**; the "a_bad ≈" reading and the "conservative" direction **REFUTED** (agreeing with Codex)
*Where:* HW l.183 "SQ's θ_0 ≈ 10⁻⁸/C_D²", l.604 "a_bad = c_♭τ_♭² ≤ (1/640)(θ_0/C′)² ≈ 5·10⁻²³/C_D⁴"; SQ l.212 "θ_0 ≈ 10⁻⁸/C_D² at
C_D = 2", SQ l.216 "[RSQ1-fix M-6] … θ_0 ≈ 3·10⁻⁸/C_D² (the '10⁻⁸/C_D²' above is 3× low)".
- (1/640)(θ/53)²: 5.562477750·10⁻²³ at θ = 10⁻⁸; **9/17977600000000000000000 = 5.006229975·10⁻²²** at θ = 3·10⁻⁸; ratio exactly 9;
  ratio to HW's printed 5·10⁻²³ is 28125/2809 = 10.0125 (A6). SQ's own "≈ 3·10⁻²³ (C_D = 2)" is B/16 = 3.13·10⁻²³ ✓.
- But l.604 displays an UPPER BOUND on a_bad on the branch ε_1 ≥ C′τ_♭, with τ_♭ a minimum of several entries (SQ l.294 Lemma
  DESC: "Fix τ ≤ min{τ_F, τ_R, θ_0/C′, …}"). Correcting θ_0 raises the cap; it does not make a_bad ≈ 5.01·10⁻²² and does not show
  the old figure "under-states the suppression". At the live ε_1 ≲ 6.7·10⁻⁴⁰ the route is on the ε_1 < t_pr branch
  (a_bad = c_prε_1² ≈ 2.5·10⁻⁸⁵), so l.604's branch is not live and nothing moves. HW **l.826** repeats the stale "≈ 5·10⁻²³/C_D⁴"
  and is missing from SYMBOLS' rename/fix table (Codex SYMBOLS F3 found the same).

## F19 (T11) REVIEW_HW_S5 — the other banked verdicts, re-judged
| verdict in REVIEW_HW_S5 | my verdict | basis |
|---|---|---|
| S5-11 satisfiable, g-free ceiling | **CONFIRMED** | F1 |
| S5-12 (S2) ≡ REL-boot ≡ HIST-sum; (T) ≡ n_H | **CONFIRMED** (numbers A2); its n_H row uses B_0 = c_f while its HIST-sum row uses c_f + 2 — immaterial (F7) | A2 |
| S5-13 does not bind against DX′, ~55 orders | **CONFIRMED** (currency argument supplied, F1) | A3, A4 |
| S5-14 (1) free lever 6561 → 2401; g²_CRC → 1.338e-96 | **CONFIRMED** (b_n = 7471609475c_+ reproduces by hand: 2401·81·38418 + 38417) | hand |
| S5-14 (2) / S5-24 "the multiplicative factor may be removable; excess depth-stable; N_1∘π drives both sets to the same fixed point within two levels" | **REFUTED** (Proposition SH-neg, F2; the review's evidence sampled random positions) | G-A |
| S5-16 (1)-(2) allowance and level-range deltas | **CONFIRMED** | F5 |
| S5-16 (3) universal F_< has sup strength; restrict it | **CONFIRMED, sharpened** to explicit counterexamples | F6 |
| S5-19 finer-first order reinstates the node-A law mismatch | **REFUTED** (premise false: PLD l.1736 writes the law with Π_{k′<k}Φ_{k′}) | F17 |
| S5-6, S5-7 SH-att / COL constants, b_n, b_D | **CONFIRMED** (re-derived; A1 integers) | hand, A1 |
| S5-8 … S5-10 CRC-2T induction, step algebra, (S1) arithmetic | **CONFIRMED** at the steps re-walked (F17); not re-proved in full | hand |
| S5-21 symbol collisions c_f, C_ℓ, c_U | **CONFIRMED** by reading HW l.1273/1690/1543 and PLD l.1417 | read |
| S5-23 Part A reproduces | **CONFIRMED** | A1, A2 |
| S5-1 … S5-5, S5-15, S5-17, S5-18, S5-20, S5-22, S5-25 | **NOT-VERIFIED** (spot-read only; no defect noticed) | — |

## F20 (T12) REVIEW_PLD_S5 — banked verdicts, re-judged
| verdict in REVIEW_PLD_S5 | my verdict | basis |
|---|---|---|
| S5-6 FT^far's hypothesis stronger than its proof uses | **CONFIRMED** | F8 |
| S5-7 COL-DEC | **CONFIRMED** (re-derived; it is what defeats BUF-CC's consequence) | F4 |
| S5-8 / B1 the "any w" interface is expected false; restrict to buffered weights | **CONFIRMED** (and the same disease recurs as universal F_<, F6) | F6 |
| S5-9 (a) slice does not type-check; union currency needed | **CONFIRMED** | PATCH (ii) |
| S5-9 (b) / B2 second clause: "‖x(S)‖_sh ≤ ‖S‖_sh + c|S| with c depth-free … plausible (the deep shadows of x(S) and S coincide)"; "in the union form the recursion does close with c(k) = c(k−1)" | **REFUTED** (F9: excess 81 + 175D; at D = 20000 it exceeds 1 + Δ_sh) | G-B |
| S5-10 the slice is a regression | **CONFIRMED** | read |
| S5-25 no status error on c_lcr | **CONFIRMED** | F14 |
| S5-26 PLD S5 does not supply (E2^𝔉) | **CONFIRMED** (PLD §18.1 reaches the same verdict) | read |
| S5-27 naming clash | **CONFIRMED** | read |
| S5-1 … S5-5, S5-11 … S5-24 (DIL-L, MD, p5 arithmetic, CD) | **NOT-VERIFIED** (session-5 material outside this batch's claims; not re-derived) | — |

## F21 (T16) HW_LOG session 6, PLD_LOG sessions 6-7 — **CONFIRMED** as records; they inherit the refuted statuses
Byte counts and order match the files as they stand (HW.md 254211 bytes; PLD.md 389932 bytes; w6/p6/p7 criteria hashes as logged;
criteria written before scripts per the logs). The status lines repeat claims refuted above: PLD_LOG s6 "the union-form excess
line (b′)" and "No statement in §18 depends on the numerical value of Δ_sh" (true of the value, false of the depth-freeness it
relies on, F9); PLD_LOG s7 "Lemma DLR and Theorem W-FREE (the far weight is eliminated exactly …)" (F10) and "price ×82 not
×17, settling HANDOFF's cross-lane disagreement 1" (F4); HW_LOG s6 "it persists at ×11.2 once node A's ring is bought" (F7).

## F22 (T17) Codex reviews used — agreement stated
- **CODEX_REVIEW_SYMBOLS F1 (66/90/122 PROVEN arithmetic at the selected ε; not uniform as ε → 0; do not land "66" as a constant)
  — AGREE** (F16; I add that the number sits in a retired architecture and flips under the pending KN adoption).
- **CODEX_REVIEW_SYMBOLS F3 (×9 coefficient CONFIRMED; "cap-as-rate" and the conservative-direction argument REFUTED; HW l.826
  omitted) — AGREE** (F18).
- **CODEX_REVIEW_SYMBOLS F2 (SY1-2's NO-DEFECT branch is not the negation of its target) — AGREE** as far as it touches F16: the
  ε_1 = 2 control discriminates large from small depths, not right from wrong; my A5 compares each computed depth with its claimed
  value directly, which is the repair Codex asks for.
- **CODEX_REVIEW_DECADES l.198 / l.652 (×9 θ_SUP correction CONFIRMED, 10.0125 against the printed value) — AGREE** (A6 gives the
  same exact rationals).
- Both files read as complete on disk (SYMBOLS ends with its "Stdout summary"; DECADES with its verdict table). No other Codex
  review touches HW §34-§41 or PLD §18-§19.

*(Precision added to F7: HW l.1690 defines B_0 = c_f + 164ε′ + log(4/3) ∈ (c_f + 0.28, c_f + 1.29], so neither "c_f" nor "c_f + 2" is
exact; both are bounds (c_f + 2 the safe one). n_H and n_T agree to 6 significant figures either way; nothing turns on it.)*

---

# SUMMARY TABLE (every claim in the batch, with its verdict)

| id | claim (file, locating string) | verdict | finding |
|---|---|---|---|
| r55h-01 | REVIEW_HW_S5 S5-11: smallness condition satisfiable, g-free ceiling | CONFIRMED | F1 |
| r55h-02 | REVIEW_HW_S5 S5-13 / HW §35.7 (iii) / HANDOFF: does not bind vs DX′ (×1.96e55; ×3.59e56) | CONFIRMED (currency argument supplied; figure convention-dependent, 55.3-57.8 decades) | F1 |
| r55h-03 | HW Prop SH-neg: additive form false ("lever (b) refuted") | CONFIRMED | F2 |
| r55h-04 | HW l.1940 / l.2283 "π^r(y) stays at distance 1 from π^r(z) for ever" | REFUTED (distance 0 from r = 3) | F2 |
| r55h-05 | HW l.1901 "the samples force a multiplicative factor ≥ 5.714" | REFUTED (unsupported) | F2 |
| r55h-06 | HW "lever (a) beaten": SH-1, SH-2, COV, H-geo′, SH-att′ (81), COL′ | CONFIRMED | F3 |
| r55h-07 | HW Lemma RING inequality |sh(N_1X)| ≤ 16|sh(X)| | CONFIRMED | F4 |
| r55h-08 | HW: ring price ×17 (c_+ = c_A + 17c_U) as a sufficient price; §41 item 4 | CONFIRMED (not sharp: the needed ring is free) | F4 |
| r55h-09 | PLD §18.4 / §19.1: ring price ×82 as THE price | REFUTED (valid only as a loose bound) | F4 |
| r55h-10 | PLD §19.1/§19.10/§19.11, HANDOFF: "the closed column is what the proof uses; reverse HW §41 item 4; settled" | REFUTED | F4 |
| r55h-11 | PLD Finding (BUF-CC): §18.7.0's level-(k−1) generators not certified by "N_1(𝒜) R-free" | CONFIRMED | F4, F12 |
| r55h-12 | later "g²_CRC at the ×82 ring" (1.85835e-96) as the HW-route ceiling | REFUTED (×82 pessimistic; binding is 3.96620e-95/c_+ with HIST as written; no verdict flips) | F4 |
| r55h-13 | EPS1_SWEEP cites HW l.2006 (×17 row) for the ×82 figure (l.2007) | CONFIRMED | F4 |
| r55h-14 | the HW/PLD allowance-currency defect exists; found by both reviews | CONFIRMED | F5 |
| r55h-15 | "NA-PRICE^{E+} generates no allowance, only transmits" | CONFIRMED | F5 |
| r55h-16 | same for NA-PRICE^E (i) (HW l.2099; PATCH (iv) l.2384) | REFUTED | F5, F9 |
| r55h-17 | HW §37 (E2^𝔉′) and PLD Cor. E2-RED repairs match (session 6) | CONFIRMED (as a match) | F5 |
| r55h-18 | F_< universally quantified, "free" (PLD Delta 3/M-7, 𝔏^buf, (CEM^{COL}), E2-RED; HW §37) | REFUTED (false statements) | F6 |
| r55h-19 | interface delivered at every j ≥ max{k_0, 1} | REFUTED at j = k_0 (as stated) | F5 |
| r55h-20 | HW §35.7 table (15 integers, 10 enclosures) | CONFIRMED | F7 |
| r55h-21 | HW "÷311.2 on n_♯ at every ring value" | REFUTED (311.12 at c_+ = 1; immaterial) | F7 |
| r55h-22 | HW "n_H = 2.09688e96" (×17); REVIEW_HW_S5 S5-12 n_H row | REFUTED as printed (B_0 convention; immaterial) | F7 |
| r55h-23 | HW §35.7 (i): breach "does NOT disappear … ring costs ×17 on top" | REFUTED as attributed (residual is HIST's 38417) | F7 |
| r55h-24 | PLD s6 law conversion closed: (C_S′), FT^far′, FAR, BUF | CONFIRMED | F8 |
| r55h-25 | PLD §18.5 (b′) depth-free Δ_sh; "compounding is NOT a reason"; §18.11 UPGRADE | REFUTED | F9 |
| r55h-26 | PLD s7 "(CEM-2) dissolved": READ (iii), DLR, W-FREE, "(BCH-1) strictly smaller" | REFUTED | F10 |
| r55h-27 | PLD s7 "(LCR) restated past its own impossibility" | REFUTED (as argued) | F11 |
| r55h-28 | PLD s7 READ (i), (ii), (iv)-(vi); Lemma MARG | CONFIRMED | F12 |
| r55h-29 | PLD s7 Lemma DOM | CONFIRMED (constant slip 2Rg_K² → 4Rg_K², immaterial) | F12 |
| r55h-30 | PLD s7 DOM′, Theorem AT, ACT-EQ (i)-(ii), TRADE (ii), OUT (identity), (ACT) withdrawal | CONFIRMED | F12 |
| r55h-31 | PLD s7 ACT-EQ (iii) "(ACT) strictly stronger than (CEM^{COL})" | NOT-VERIFIED | F12 |
| r55h-32 | PLD s7 Theorem L0: 645 transverse dimensions; log C_fc^{(0)} = 13.7255 | CONFIRMED | F12 |
| r55h-33 | PLD s7 Theorem L0 (ii): conditional law "× 1{ζ_Q = 0}" | REFUTED | F12 |
| r55h-34 | PLD s7 "(0a) is the weaker, and strictly. PROVEN-HERE" | NOT-VERIFIED (a route ranking, not an implication) | F12 |
| r55h-35 | PLD s7 request "state the level-0 clause as (0a) only, drop (0b)" | REFUTED (CRC-2T′ at j = 0 is (0b)-shaped) | F12 |
| r55h-36 | PLD s7 "(NP-F13) is REFUTED" | NOT-VERIFIED | F12 |
| r55h-37 | PLD s7 route (ρ2) (ARGUED in file) | NOT-VERIFIED (its ×82 should read ×1) | F12 |
| r55h-38 | PLD s6 NA-PRICE^{E+} (i), Cor. E2-RED, Prop ONE, Prop SPLIT as implications | CONFIRMED (logic; hypothesis false as quantified, r55h-18) | F13 |
| r55h-39 | PLD s6 §18.5 CHAIN verdict (NP-F6) | CONFIRMED | F13 |
| r55h-40 | PLD s6 §18.7.2 (α)/(β): the buffer-good event cannot give a g-free constant | CONFIRMED (qualitatively) | F13 |
| r55h-41 | PLD §18.8: c_lcr's value not load-bearing; (iii) no PROVEN item rests on it | CONFIRMED | F14 |
| r55h-42 | PLD §18.8: "enters only against b_n"; "log c_lcr ≤ 10⁹ ⇒ < 5%" (and §19.4/§19.5 clause 5) | REFUTED (×16 on (S2) at current b_n; ×814 on (S1) already at s5) | F14 |
| r55h-43 | "4.489e15" as the event-route gap (PLD §18.7.2, §19.6 (i), HANDOFF item 3) | REFUTED as a currency (arithmetic exact at a stale g_K² = 1e-94; ≥ 9.28e17 / 1.80e73 at programme couplings) | F15 |
| r55h-44 | SYMBOLS: PLD l.1098 m_τ = 3 wrong; 66/90/122 at RLARGE's threshold | CONFIRMED (with scope corrections) | F16 |
| r55h-45 | SYMBOLS: HW l.604 coefficient ×9 (5.01e-22) | CONFIRMED | F18 |
| r55h-46 | SYMBOLS: "a_bad ≈ 5.01e-22", "conservative" direction | REFUTED (it is a cap on a non-live branch) | F18 |
| r55h-47 | HW §38 "All eleven are applied" (E2-2) | REFUTED (E2-2 reversed) | F17 |
| r55h-48 | HW §37 TF-2 adjudication (node A right vs S5-19) | CONFIRMED | F17 |
| r55h-49 | HW CRC-2T′ (s6 replacements), §35.6 (c), §36 V2 (a) NOT DELIVERED, §41 items 1-3 | CONFIRMED | F17 |
| r55h-50 | HW §37 narrowing of §24.3's doubt (S5-17) | NOT-VERIFIED | F17 |
| r55h-51 | REVIEW_HW_S5 S5-14 (2) / S5-24 (factor removable; excess depth-stable) | REFUTED | F19 |
| r55h-52 | REVIEW_HW_S5 S5-16 (3) (universal F_< has sup strength) | CONFIRMED | F19 |
| r55h-53 | REVIEW_HW_S5 S5-19 (finer-first reinstates law mismatch) | REFUTED | F19 |
| r55h-54 | REVIEW_HW_S5 S5-6, S5-7, S5-8…S5-10, S5-12, S5-14 (1), S5-21, S5-23 | CONFIRMED | F19 |
| r55h-55 | REVIEW_HW_S5 S5-1…S5-5, S5-15, S5-17, S5-18, S5-20, S5-22, S5-25 | NOT-VERIFIED | F19 |
| r55h-56 | REVIEW_PLD_S5 S5-9 (b) / B2 second clause (depth-free union excess "plausible") | REFUTED | F20 |
| r55h-57 | REVIEW_PLD_S5 S5-6, S5-7, S5-8/B1, S5-9 (a), S5-10, S5-25, S5-26, S5-27 | CONFIRMED | F20 |
| r55h-58 | REVIEW_PLD_S5 S5-1…S5-5, S5-11…S5-24 | NOT-VERIFIED | F20 |
| r55h-59 | HW_LOG s6, PLD_LOG s6-s7 as records | CONFIRMED (inherit refuted statuses) | F21 |

**Counts: 29 CONFIRMED, 7 NOT-VERIFIED, 23 REFUTED (59 rows).**

# FOR THE LEAD

## Every REFUTED item, with its correction
1. **r55h-04** HW l.1940/l.2283: the projections do not stay at distance 1; d_r = 8, 3, 1, 0, 0, … — they coincide from r = 3, and the
   shadows still never merge. SH-neg itself stands.
2. **r55h-05** HW l.1901: delete "the samples force a multiplicative factor ≥ 5.714"; the only forced lower bound is 4/3 (SH-neg).
3. **r55h-09/-10/-12** The ring: what the proof needs is HW's OPEN ring at level j (it already contains PLD's level-(j+1) closed
   column, since π(N_1(col Γ)) = N_1(Γ)); (D2) gets its level-(j−1) property from COL-DEC, not from a closed ring. Its true cost is
   nil (π^r(N_1X) ⊆ Σ^r(X), and Col(Y) ⊆ Col(N_1X)): c_+ = c_A + c_U, (S2) = **1.52362·10⁻⁹⁴/c_+**; with HIST's 38417 the HW-route
   binding ceiling is HIST-sum at **3.96620·10⁻⁹⁵/c_+**. ×17 is a valid loose bound; ×82 a looser one; even a closed ring at
   level j would cost only a per-cube surcharge (b_n + 6480c_U), not ×82. HW §41 item 4 stands; PLD §19.11 item 1 and HANDOFF's
   "settled" are withdrawn.
4. **r55h-16** "NA-PRICE^E/E+ transmit only": true for E+ only; for E (i) Lemma MD's push-down changes the allowance by up to a
   factor ≥ 256/81 (bounded by ‖x(S)‖_sh ≤ 16‖S‖_sh + 81|S|).
5. **r55h-18** F_< must not be universally quantified: restrict to the specific capped spectators Π_{k′<j}Φ_{k′} (what PLD §17.2's
   law already carries) or to bounded F_< measurable off region(A). As written, (E2^𝔉′), (CEM^{COL}), (ACT′), (LCR^act′) and
   (BCH-1) are false (conditioning the finer fields forces the coarse defect / column energy).
6. **r55h-19** E2-RED as stated delivers j ≥ max{k_0 + 1, 1}; j = k_0 returns once F_< is restricted (GEO (iv) handles Φ_{j−1}).
7. **r55h-21** "÷311.2 at every ring value" → ÷311.12 at c_+ = 1 (÷311.17 at ×17 and ×82).
8. **r55h-22** n_H at ×17 is 2.096918·10⁹⁶ at B_0 = c_f + 2 (2.09688 is at B_0 = c_f); REVIEW_HW_S5's S5-12 n_H row likewise uses
   B_0 = c_f (9.991019e96) against its own HIST-sum row's c_f + 2 (which gives 9.991057e96). The exact B_0 (HW l.1690) lies between.
9. **r55h-23** The (S2) breach of 10⁻⁹⁴ disappears once the ring is priced correctly (1.52·10⁻⁹⁴, +0.18 decades); the residual
   ×2.52 breach is HIST-sum with HIST's unsharpened 38417 (W-F3), not the ring.
10. **r55h-25** PLD §18.5 (b′) is false: at Q = (3w, 3w, 3w, 3w), w = (3^D − 1)/2, the excess ‖x(S)‖_sh − ‖S‖_sh = 81 + 175D (exact;
    3500081 > 1 + Δ_sh at D = 20000). True bound: ‖x(S)‖_sh ≤ 16‖S‖_sh + 81|S| (multiplicative; ≥ 256/81 needed). "Compounding is
    NOT a reason" and the §18.11 UPGRADE fall; §16.6 (b)/§16.7's per-cube Δ_sh (session 4) falls with them.
11. **r55h-26** (CEM-2) is not dissolved: the pattern constraint is the n_♯-cluster indicator of HW §13.1 (l.614), not
    Π1{ζ_x = 0}; the column's conditional law depends on outside defect clusters that the far weight reads; and (EQ-bc) with an
    existential 𝔉_out-measurable charge is vacuous (𝔟_Q := sup_λE_λ[𝔞^col_Q|𝔉_out]). Correct status: (CEM^{COL}) ⇐ (ACT′); the
    weighted-law decoupling is the residual, relocated, not removed.
12. **r55h-27** (LCR^act′) is not "past the impossibility" because it is a first moment: by §19.5's identity the λ-tilted first
    moments integrate to the log of the exponential moment, and the forced-curvature mechanism bounds both. Only the weight-class
    restriction (already in (CEM^{COL})) separates it from §16.7's (LCR); and it inherits r55h-18.
13. **r55h-33** Theorem L0 (ii): the level-0 conditional law carries the n_♯-cluster indicator (coupling Γ's cubes and outside
    defects), not "× 1{ζ_Q = 0}".
14. **r55h-35** Do not drop (0b): CRC-2T′ step (5) at j = 0 (and Cor. CRC-HW at k = 0) is (0b)-shaped; (0a) is TEL-f's level-0
    window. Both are consumed.
15. **r55h-42** PLD §18.8 (ii)(5): "log c_lcr ≤ 10⁹ ⇒ < 5%" is stale — at today's b_n, 10⁹ moves (S2) by ×16.2; the 5% threshold
    is log c_lcr ≲ 3.3·10⁶; and in (S1) log C_A enters against c_+c_att(ρ), not b_n.
16. **r55h-43** "4.489·10¹⁵" is (ε_1/g_K)² at g_K² = 10⁻⁹⁴; at the HW-route binding value it is ≥ 9.28·10¹⁷ and at DX′ 1.80·10⁷³ —
    quote it as "≥ 10¹⁷ (HW route), 10⁷³ (DX′)"; §19.6 (i)'s "2.2445·10⁶ in the log" becomes "≥ 10⁶³".
17. **r55h-46** SYMBOLS §4.4: HW l.604 is a cap (a_bad ≤ (1/640)(θ_0/C′)²) on the non-live branch ε_1 ≥ C′τ_♭; correct the cap
    to 5.006·10⁻²²/C_D⁴ (also at HW l.826, which SYMBOLS' table omits); do not write "a_bad ≈" or "conservative".
18. **r55h-47** HW §38's "All eleven are applied; none is declined": [RHW5-fix E2-2] was reversed, not applied (r55h-18).
19. **r55h-51** REVIEW_HW_S5 S5-14 (2)/S5-24: the multiplicative factor is not removable (SH-neg); random-position sampling hid it.
20. **r55h-53** REVIEW_HW_S5 S5-19: PLD §17.2 does write its law with the finer capped spectators; the TF-1 worry was unfounded.
21. **r55h-56** REVIEW_PLD_S5 S5-9 (b)/B2: the depth-free union excess it asked for is false (item 10); keep B2's currency clause.

## What PROOF.md's tally / HANDOFF's critical path should say differently
- **PROOF.md l.6910-6916 ("Node A … (E2^𝔉)'s law-conversion obstruction is closed … The HW/PLD interface is repaired … The chain
  waits on (CEM-1)/(CEM-2) and the level-0 clause"):** the law conversion is closed (CONFIRMED) and the allowance currency is
  repaired (CONFIRMED), but the repaired statement (E2^𝔉′) is **false as quantified** until F_< is restricted (r55h-18), it is not
  delivered at j = k_0 as stated (r55h-19), and the level-0 hole is two-shaped ((0a) AND (0b)). PLD session 7's replacement of
  (CEM-2) by (EQ-bc) + (BCH-1) is **not** an advance (r55h-26): the residual is the weighted-law decoupling inside (ACT′)/(CEM^{COL}).
- **Session-7 counted items (PLD [E7]):** (1) should not be counted as PROVEN (READ (iii), DLR, W-FREE refuted; BUF-CC's
  consequence refuted); (2) counts only as identities; (3) counts for the dimension count and window constant only.
  **Session-6 [E6] (1)-(2):** stand (implications), with PATCH (iv) restricted to E+. **The uncounted §18.5 (b′) is false.**
  **HW [HW-12]:** stands (all seven lemmas/propositions CONFIRMED; two sentences struck, r55h-04/-05).
- **HANDOFF "Two cross-lane disagreements" item 1:** reverse — HW was right; the ring the proof needs is the open one and it is
  free; ×82 figures (and the "×82 closed-column numbers" PROOF l.76 compares against) are pessimistic by ×82 in (S2), ×21 in the
  HIST-limited ceiling. No NOT-BINDING verdict changes.
- **HANDOFF critical path item 3:** replace "(CEM-1) and (CEM-2) … gap of 4.489e15" by: "(CEM^{COL}) (or (ACT′)) with F_<
  restricted to the history spectators — its screening content, a decoupling under the weighted past law, is the residual
  (PLD s7's W-FREE does not remove it); the event-route gap is ≥ 10¹⁷ at the HW-route coupling; level 0 needs both (0a) and (0b)
  shapes, and j = k_0 must be checked once F_< is fixed."
- **HANDOFF "WITHDRAWN" item 1 (lower g_0):** stays withdrawn (r55h-02), now with the uniform-in-K reason stated.

## Codex verdicts used
CODEX_REVIEW_SYMBOLS F1 — agree; F2 — agree (as it bears on F16); F3 — agree; CODEX_REVIEW_DECADES l.198/l.652 (×9) — agree.
I disagree with none of the Codex verdicts I used. Both files are complete on disk.

UTC end: 2026-10-28 (see the reply timestamp); every check file named above exists under checks/r55h_*.
UTC end (actual): 2026-10-28T23:04:11Z. Files written by this reviewer: REVIEW55_HWPLD.md; checks/r55h_geo_criteria.md, r55h_arith_criteria.md, r55h_ring_criteria.md, r55h_geo.py, r55h_arith.py and their _out/_err files. No git command was run.
