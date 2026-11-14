Reviewer model: claude-opus-5-5

# REVIEW55_CONST — Opus 5.5 re-review of batch C5, the constants chain (q -> C_T -> C_D -> eps_1)

UTC start: 2026-10-28T22:12:49Z
Batch: C5. Check-id prefix: `r55k_`. Deliverable (the only file written in the lane besides
`checks/r55k_*` criteria/scripts/outputs, criteria file always written before its script):
`$L/REVIEW55_CONST.md`. No git. Append-only.

Files in scope: CONST_T.md, STAR_CONST.md, EPSSTAR.md, TAUFLAT.md, EPS1_SWEEP.md, EPS1_EXEC.md, QFIX.md.
Codex gpt-6-astra/max inputs: CODEX_REVIEW_QFIX.md (380 lines, mtime 18:11:53 local),
CODEX_REVIEW_DECADES.md (142 lines, mtime 18:10:33 local) — both possibly still being written; to be
re-read before finishing.

## PRE-STATED (written before any derivation; statements only)

Targets (each gets CONFIRMED / NOT-VERIFIED / REFUTED):

K1  CONST_T: "q = 8 is the worst admissible choice".
K2  CONST_T: "all hold for every q > 4" (QFIX says false on (4,8)).
K3  STAR_CONST: the energy-inequality constants; C_1 = 5699.6 is computed while §8.3 quotes a figure
    computed at a supplied C_1 = 20 (ratio x287). Which C_1 does the quoted figure belong to?
K4  EPSSTAR: A_c*gamma_c bounded constant-free ("every supplied constant cancels").
K5  EPSSTAR: C_T = 5.29e12 at q = 12.
K6  EPSSTAR l.525 vs l.521 + l.527 (QFIX's claim): inconsistent by exactly sqrt(10);
    t_pr >= 9.52e-35 not 3.01e-35; hence C_D <= 1.78e13 not 3.17e13.
K7  TAUFLAT: the conflict confirmed and (MS-Sob) returned to the critical path.
K8  TAUFLAT: "0.080 decades of room" in C_T, vs EPS1_EXEC's 0.578 (over q).
K9  EPS1_SWEEP: "eps_1 is five symbols".
K10 EPS1_SWEEP: option C "SAFE WITH NAMED CONDITIONS (C1)-(C7)".
K11 EPS1_SWEEP: the a_RS ceiling already binds by 15.6 decades — arithmetic only, and the eps_1
    value it is evaluated at (whether a_RS is consumed at all is another batch's question).
K12 EPS1_EXEC: (C6) discharged by an exactly factorising 2x2 table (old/rerun class x pre-TB-1/TB-1)
    of the four live eps_1 values, giving eps_1 <= 6.7e-40 at RLARGE l.72.
K13 EPS1_EXEC: (C3) has its sign inverted (PLD l.995's 2 m_* g / eps_1 rises as eps_1 falls).
K14 EPS1_EXEC: EPS1_SWEEP's replacement value 9.38495112638e-45 is above its own bound by 2.34e-13.
K15 QFIX: q was never chosen on the merits.
K16 QFIX: 14 consumers, 13 want q large; no upper constraint anywhere.
K17 QFIX: consumer floor q >= 12 because q = 11 fails by x1.16.
K18 QFIX: a_RS proportional to C_D^{-8}.
K19 QFIX: total lever 24.089 decades.
K20 QFIX: argmax q = 1000.
K21 QFIX: new target eps_1 <= 3.8e-43 (3.8235e-43).
K22 QFIX: the "(0.5-0.9)*10^3" band is really c_N.
K23 Codex DECADES vs QFIX: a q = 1000 cutoff near 1.4695e-44 below the quoted 3.8235e-43 — reconcile.
K24 Codex CODEX_REVIEW_QFIX / CODEX_REVIEW_DECADES: agree/disagree with each finding used.
K25 Every other PROVEN / PROVEN-HERE claim, REFUTED / FALSE / struck verdict, and decision-changing
    number in the seven files — to be enumerated after reading; any target added later is marked
    "added after reading, before derivation".

What counts as a refutation (fixed now):
- Numeric claim: re-derived from the formula at the cited file:line (located by string) with exact
  rational arithmetic, logarithms by rigorous rational interval bounds. REFUTED if the exact value is
  outside the claimed figure's rounding interval (e.g. "5.29e12" = [5.285e12, 5.295e12)), or a claimed
  inequality fails, or the claimed decade count is outside its last stated digit by more than rounding.
- Currency: REFUTED (or flagged) if the figure is right but is evaluated at a different value of a
  symbol (different C_1, eps_1, q, ...) than the comparison it is used in assumes — verified by file:line.
- Quantifier claims ("worst admissible", "for every q > 4", "no upper constraint anywhere",
  "13 of 14 want q large"): REFUTED by an exhibited counterexample with exact arithmetic, or by a
  located constraint/consumer that contradicts the count.
- "Constant-free" claims: REFUTED if a supplied constant survives in the final bound after correct algebra.
- "Exactly factorising 2x2 table": REFUTED unless v11*v22 = v12*v21 holds exactly (or to the precision
  claimed) with rows/columns matching the stated classes by file:line.
- Sign claims: REFUTED if the monotonicity derived from the formula has the opposite sign.
- NOT-VERIFIED when the inputs cannot be located, or settling the claim needs material I could not check;
  I will say exactly what is missing.

### PRE-STATED addendum — targets added after reading the seven files and both Codex reviews, before any derivation (UTC 22:4x)

K26 Radius-budget consistency of the schedule factor F = 175.8 (CONST_T §3.2, budget R/2 − 4, i.e. Stage 2 from
    r_0 = R − 4) with Stage 1's output ball (SQ.md l.1496: V_c ∈ ℓ⁴(B_{3R/4−3}); EPSSTAR §3.1 keeps that ball). Every
    C_T number in STAR_CONST/EPSSTAR/QFIX uses F = 175.8. Refutation: Stage 2's first radius lies outside the ball on
    which A_cγ_c is controlled, and F recomputed on an admissible budget differs.
K27 EPSSTAR l.608 "floor over all δ-budgets … C_T ≥ 4.4·10¹² at q = 12" (the floor TAUFLAT's 0.080 is measured from).
    Refutation: an admissible allocation with C_T < 4.4·10¹², or the stated reasoning (c_s ≥ 319.2) giving another number.
K28 TAUFLAT §2: the 52.077-decade gap, the C_D ≤ 455.283301 window, the 9.707-decade shortfall, and "option A dead".
K29 EPS1_EXEC §4.4's q = 8 row (−2.761 decades) — which C_T it uses.
K30 QFIX §5.4 / §12.3: "θ_G does not become binding until q > 5.573·10²⁶" — against which comparator.
K31 QFIX census row 4 (A_cγ_c "wants q large") — Codex says it reverses at q = 432·c_s.
K32 QFIX §7.2's "3.5·10⁻⁴³ at q = 100" — whether it is below its own ceiling.
K33 STAR_CONST/EPSSTAR "C_1·C_V ≥ 1 forced" (CONST_T §6.1) vs STAR_CONST's C_V^source = 0.072 — whether CONST_T's
    q = 8 negative (C_T ≥ 1.27·10¹⁴) survives.

Check files will be `checks/r55k_1_criteria.md` (written before any script) → `checks/r55k_1_const.py` →
`checks/r55k_1_out.txt`. Any later probe gets a new id and its own criteria file first.
(Provenance correction, appended: the addendum header above says "UTC 22:4x"; `date -u` at the moment it was appended
read **2026-10-28T22:35:40Z**. No derivation had been written or run at that time.)

---

## 0. Method, check files and disclosures (written after the checks ran)

**Checks.** All arithmetic is in three plain-python scripts that share one interval library (`fractions.Fraction`
+ `math.isqrt`; log by 2·atanh series with explicit tail bound, exp by Taylor with explicit remainder, outward
rounding to 300 bits; sanity gates log10 2 + log10 5 ∋ 1, exp(ln 2) ∋ 2, (√2)² ∋ 2 all pass). Every verdict is
decided on an interval. Order of files (UTC): this file's PRE-STATED 22:12:49 → addendum 22:35:40 →
`checks/r55k_1_criteria.md` 22:36:31 → `checks/r55k_1_const.py` 22:40:51 → run 1 22:42:29 (aborted in section G on
`I ** int`; output kept as `checks/r55k_1_run1_abort_out.txt` / `_err.txt`) → one-line fix (an integer `__pow__`,
nothing else) → run 2 22:43:28 (`checks/r55k_1_out.txt`; its first 152 lines are byte-identical to run 1's) →
`checks/r55k_2_criteria.md` 22:44:47 (POST-HOC, written after reading r55k_1_out) → `checks/r55k_2_posthoc.py` run 1
aborted on a display call (`checks/r55k_2_run1_abort_out.txt`, no verdict produced) → display fix → `r55k_2_out.txt`
→ `checks/r55k_3_criteria.md` 22:54:02 (POST-HOC) → `checks/r55k_3_sharp.py` → `r55k_3_out.txt`. Runtimes 11 s,
9 s, 38 s; single thread, nice 10, no numpy/BLAS, no lock needed.

**Disclosure 1 — a defect in my own verdict code (r55k_1 item A3).** A3 prints FAIL. The cause is mine: at q = 8 the
quarter-split constant c′_ϑ equals **exactly 1** (ϑ = ½: (1 − ½)·2¹ = 1; r55k_2 P2, exact Fraction), its interval
straddles 1, and my code tested `hi ≤ 1` instead of the criteria file's own general rule (FAIL only if the whole
interval violates). By the pre-registered rule A3 is UNDECIDED at q = 8 and PASS at the other seven grid points; I
settle it analytically in K2 below (c′_ϑ ≤ 1 ⟺ q ≥ 8). The printed FAIL is left unaltered.

**Disclosure 2 — the B1 diagnostic line "printed c_s, c_g inside the enclosures: False False"** is an ill-posed
test (a 19-digit decimal rounding of an irrational number cannot lie inside a 10⁻⁸⁸-wide enclosure); it carries no
verdict. The enclosures c_s ∈ [411.9229708842, 411.9229708843], c_g ∈ [5699.632830341, 5699.632830342] agree with
the printed values to every displayed digit.

**Disclosure 3 — r55k_2 and r55k_3 are POST-HOC.** They were designed after r55k_1 exposed the radius-budget
problem (K26) and after I noticed the telescope-exponent looseness while writing it up. Each had its criteria file
written before its script, and each reports its pre-registered verdicts unaltered.

**Symbol discipline used throughout** (defect 1). q = the Moser exponent of EPS-T (SQ.md l.1460-1462, "Fix q := 8"
at l.1622), never the RES-dec decay ratio q (SQ l.1524) that sits in B_0 = 46.8. C_1 = CONST_T's single (★)
prefactor; STAR_CONST splits it into c_g (cut-off prefactor), c_s = C_1·C_V^source, c_K, c_RB. ε_* = EPS-T's
threshold (EPSSTAR's symbol 1), never N5-sf0's 2.476·10⁻¹³/C_Δ. ε_1 = RLARGE §0's χ_Q cut (RLARGE l.58) unless
stated. θ_0^SUP = 1/(2C_err) (SQ l.188) vs θ_0^{SQ4} = min{θ_G, θ_ε} (SQ l.1622). F = CONST_T's schedule factor
R²·Π d_i^{−2/p_i}.

---

## 1. HEADLINE (new; no Codex review looked at it): every C_T number in this chain is computed on a radius schedule that Stage 1 does not support, and with a telescope bound that is loose by ×2.6-2.75. The two errors partly cancel; the ε_1 targets built on them are not safe as quoted.

### 1.1 K26 — F = 175.8 is inadmissible. **REFUTED.**

*Locating strings.* SQ.md l.1496: **"V_c ≤ C(M_3w)(1 + ε) lies in ℓ⁴(B_{3R/4 - 3}) … (Stage 1)"**; SQ l.1498 then runs
Stage 2 on r_i := R/2 + R2^{−i−3}, i.e. r_0 = 5R/8 < 3R/4 − 3 (consistent). CONST_T §3.2 table row **"optimised (mine)
| R/2 - 4 | 12 | 175.8 | R = 79"**; `checks/ct1b_moser.py` `optimised(R, dmin=12.0, budget_frac=0.5, inset=4.0)`:
S = R/2 − 4, i.e. **Stage 2 starts at r_0 = R − 4**. CONST_T §2.4 defines γ := R^{2−4/σ}‖V‖_{ℓ^σ(B_R)} — V_c on all of
B_R. EPSSTAR §3.1 keeps Stage 1 as **"ζ_1 = 1 on B_{3R/4}, supported in B_{R−4}"** and §3.5 controls
**"γ_c = R·‖V_c‖_{ℓ⁴(B_{3R/4−3})}"**, then §7.1 evaluates with **"F = 175.8, R_0 = 64"**. STAR_CONST (`sc1_cs.py`
F_CT = 175.8) and QFIX (§7.1 parametric chain "F = 175.8") inherit it.

*Why it is inadmissible.* Each Moser step i uses Hölder on V over supp ζ_i ⊂ B_{r_i}, so the V_c branch needs
‖V_c‖_{ℓ⁴(B_{r_0})}. Stage 1 delivers it only on B_{3R/4−3}. With r_0 = R − 4 the first step's annulus
(3R/4 − 3, R − 4] has no ℓ⁴ control of V_c (the only other available bound, ‖V_c‖_∞ ≤ 2ε_*, gives
R‖V_c‖_{ℓ⁴(B_R)} ≲ R²ε_*, not scale-invariant). The radius budget R/2 is shared between the two stages and CONST_T
spent all of it on Stage 2 while EPSSTAR spent R/4 − 4 of it on Stage 1.

*The admissible F, recomputed* (`r55k_1` D1-D3; CONST_T's own rule — i_* = the largest number of steps whose
smallest gap is ≥ 12, gaps ∝ 2^{−i}; F = R²(S/Λ)^{−Λ}2^σ, Λ = 2 − 2^{1−i_*}, σ = Σ_{j<i_*} j2^{−j}). Inside a block of
constant i_*, d/dR log F = 2/R − Λα/(αR − β) has a single zero (S = αR − β, β > 0), negative before and positive
after, so block endpoints suffice; all blocks up to R ≈ 10¹⁵ were scanned.

| Stage-2 budget S(R) (Stage-1 gap) | R_0 | max F (at R) | asymptote 16/α² |
|---|---|---|---|
| R/2 − 4 (CONST_T; **inadmissible**) — control, reproduces 175.8 | 32 | **175.80281** (79) | 64 |
| **R/4 − 3** (EPSSTAR §3.1's Stage-1 gap R/4 − 4; = SQ's 3R/4 output ball) | 64 | **672.02797** (155) | 256 |
| R·(1/2 − 1/8) − 3 (gap R/8 − 4) | 128 | 181.2890 (231) | 113.8 |
| **7R/16 − 3 (gap R/16 − 4)** | 256 | **105.3174** (418) | 83.59 |
| R·(1/2 − 1/32) − 3 | 512 | 81.6857 (799) | 72.82 |
| R·(1/2 − 1/64) − 3 | 1024 | 72.2227 (1566) | 68.20 |
| R·(1/2 − 1/128) − 3 | 2048 | 67.9690 (3102) | 66.08 |

A smaller Stage-1 gap is free: Theorem ES-1's margin m absorbs the larger Stage-1 constant (gap R/c − 4 with
R ≥ 16c gives the coefficient 256c² in place of 4096 = 256·4²; m rises to 94 397 at c = 16, i.e. ε_* × 0.208, still
≥ 3.0·10⁻¹⁷ against a no-change floor ≤ 2.93·10⁻³⁶), and the trivial branch costs only (R_0 − 1)².

### 1.2 The telescope bound is loose, and the loss is exactly F_max/(16/α²). (Improvement of CONST_T §2.5; not a refutation of its validity.)

CONST_T §2.4(h) gives, per step, ‖w‖_{ℓ^{p_{i+1}}} ≤ (Ĉβ_i^{4a}d_i^{−2})^{1/p_i}‖w‖_{ℓ^{p_i}} with Ĉ independent of i.
Telescoping gives **Ĉ^{Σ_{i<i_*}1/p_i} = Ĉ^{1−2^{−i_*}}**, which §2.5 replaces by Ĉ ("using Σ_{i<i_*}1/p_i < 1 and Ĉ ≥ 1"),
and then F by its maximum over R. The two maxima sit at opposite ends: F is largest where i_* is smallest, exactly
where Ĉ^{−2^{−i_*}} is smallest (Ĉ ≈ 6.4·10⁶, so i_* = 1 discounts by Ĉ^{−1/2} ≈ 4·10⁻⁴). The sharp constant of the
same route is C_T^♯ = √6·sup_R B_{i_*(R)}(8)·F(R)·Ĉ^{1−2^{−i_*(R)}}. `r55k_3` evaluates it at every block endpoint
(i_* ≤ 60) and at the i_* → ∞ limit; **in every case the supremum is the limit, C_T^♯ = √6·(16/α²)·B(8)·Ĉ**, so the
small-R maximum of F never enters and CONST_T §3.2's "the max is what enters C_T" is false (it enters only the loose
bound). Loose/sharp = 2.747 (printed schedule), 2.625 (budget R/4 − 3), 1.260 (7R/16 − 3).

### 1.3 What the chain's numbers become (q-chain exactly as QFIX §7.1: P-max, |𝒩_S| = 3, c_N = 2, C_3 = 1, m(q) with A_cγ_c ≤ 1; `r55k_2` P1, `r55k_3` S1)

| construction | C_T(12) | C_D(12) | real q with C_D = 6.7·10¹⁵ | ε_1^cut(12) | ε_1^cut(1000) | lever obj(∞)−obj(8) |
|---|---|---|---|---|---|---|
| **as printed** (F = 175.8, inadmissible; loose) | 5.2883·10¹² | 4.0518·10¹⁵ | 11.1912 | 1.2948·10⁻⁴⁴ | 3.8235·10⁻⁴³ | 24.0891 |
| as printed, sharp | 1.9252·10¹² | 1.4750·10¹⁵ | 10.0864 | 9.770·10⁻⁴⁴ | 2.885·10⁻⁴² | 24.0891 |
| **(a) EPSSTAR's own Stage-1 radii, loose** | **2.0216·10¹³** | 1.5488·10¹⁶ (FAILS 6.7·10¹⁵) | 14.5701 | 8.861·10⁻⁴⁶ | 2.616·10⁻⁴⁴ | 24.0891 |
| **(a) EPSSTAR's own Stage-1 radii, sharp** | **7.7008·10¹²** | 5.9002·10¹⁵ (passes, ×1.136) | **11.7691** | **6.106·10⁻⁴⁵** | **1.803·10⁻⁴³** | 24.0891 |
| (b) Stage-1 gap R/16 − 4, R_0 = 256, loose | 3.1576·10¹² | 2.4192·10¹⁵ | 10.5694 | 3.632·10⁻⁴⁴ | 1.0672·10⁻⁴² | 24.0920 |
| (b) same, sharp | 2.5062·10¹² | 1.9202·10¹⁵ | 10.3334 | 5.765·10⁻⁴⁴ | 1.6941·10⁻⁴² | 24.0920 |

**Consequences, stated so a hostile reader can check them.**
1. **No C_T(q) value printed in STAR_CONST §8.3, EPSSTAR §7.1, EPS1_EXEC §4.4 or QFIX §5.2 is the output of a
   consistent construction.** The q-ratios survive (the lever is 24.089-24.092 in every row), the absolute values do not.
2. **The two ε_1 targets the lane is about to land are not safe as quoted.** Under the only Stage-1 radii any file
   states (EPSSTAR §3.1), even with the sharp telescope, DESC-ε (iii) needs **ε_1 ≤ 6.11·10⁻⁴⁵ at q = 12** and
   **ε_1 ≤ 1.80·10⁻⁴³ at q = 1000**: EPS1_EXEC's P1 value **9.38·10⁻⁴⁵** violates its own clause by ×1.54 in ε_1
   (×2.36 in energy) and QFIX's **3.8·10⁻⁴³** by ×2.11 (×4.44 in energy). Both become safe only under a re-allocated
   Stage 1 such as (b), which no file states.
3. **The decisions that survive:** q = 8 stays dead (K1/K5 row below: ≥ 4.6·10¹³ even sharp); the (CLS-min) → RLARGE
   interface holds at q = 12 under (a)-sharp and (b) (margins ×1.14 and ×3.5 in C_D) but **fails under (a)-loose**,
   i.e. it is decided by an accounting step nobody wrote down; option A (sharpen C_T) stays dead for every
   allocation (K8); the q-lever is allocation-independent.
4. **What the lane must do before landing any number:** fix the Stage-1/Stage-2 split of the radius budget in SQ
   §15.1 (state ρ, the Stage-1 output radius), replace CONST_T §2.5's Ĉ by Ĉ^{1−2^{−i_*}} (equivalently use the
   asymptote 16/α² instead of max F), and carry ε_1^cut parametrically in α as well as q, C_3, c_N and (H2).

---

## 2. Findings, claim by claim

### CONST_T.md

**K1 — "q = 8 is the worst admissible choice" (CONST_T §8.1 item 1, §9 row E4; repeated at HANDOFF item 4 and in
HANDOFF's closing paragraph). REFUTED as stated; true on [8, ∞).** CONST_T itself defines admissible as q > 4
(§4 table: "q | CHOICE … free, q > 4") and tabulates q = 5, 6 as worse (1.9·10⁴⁸, 7.8·10²⁹ vs 5.1·10²⁰). Its
dominant term ½(36·C_1C_V·486)^{q/(q−4)} has base 3.4992·10⁷ > 1 and exponent q/(q−4) strictly decreasing, so
C_T(q) is strictly decreasing on (4, ∞) in CONST_T's own formula (r55k_1 A4: base⁵, base³ > base²). There is no
worst admissible q (C_T → ∞ as q → 4⁺). Correct statement: *C_T is decreasing in q; q = 8 is the worst choice in
[8, ∞), the range on which CONST_T's constants are valid as written (K2).*

**K2 — "q > d = 4 ✓ (and σ = q/2 > 2, 2σ′ < 4, ϑ = 2/σ ≤ ½, so c_ϑ ≤ 1) — all hold for every q > 4" (CONST_T
l.307-308). REFUTED (agreeing with QFIX §3.1 and Codex QFIX F01).** ϑ = 4/q ≤ ½ ⟺ q ≥ 8 (exact; 4/5, 2/3, 4/7 > ½).
The constant CONST_T actually uses, c_ϑ = (1−ϑ)(2ϑ)^{ϑ/(1−ϑ)} (λ = 1/(2ϑ)), fails ≤ 1 on (4, q_c) with
**q_c ∈ [5.175261, 5.175262]** (r55k_1 A2b; c_ϑ(5) ∈ [1.310719, 1.310721]). With s := ϑ/(1−ϑ), log c_ϑ = k(s) :=
s·log(2s/(1+s)) − log(1+s), k′(s) = log(2s/(1+s)) > 0 for s > 1, so the root is unique. *Additional point the
batch missed:* CONST_T's Ĉ = ½(A_sγ_s)^a + ½(A_cγ_c)² + 288C_1Q absorbs TWO potentials, each at "½X" (§2.4(e) is
written for one); with two branches each may take only ¼X, and the constant becomes c′_ϑ = (1−ϑ)(4ϑ)^{ϑ/(1−ϑ)}. With
h(s) := log c′ = s·log(4s) − (1+s)log(1+s): h(0⁺) = 0, h(1) = 0, h′(s) = log(4s/(1+s)) (negative for s < 1/3,
positive after), so **c′_ϑ ≤ 1 exactly for q ≥ 8 and > 1 for q < 8** (c′ = 1 at q = 8, r55k_2 P2). So CONST_T's
two-branch formula is a valid upper bound **exactly on q ≥ 8**, and the q = 5, 6 rows understate. No decision of the
lane is affected (every q in use is ≥ 8).

**CONST_T §2.4(f) — exact scale-invariance for every σ > 2. CONFIRMED** ((−2 + 4/σ)·σ/(σ−2) = −2(σ−2)/(σ−2)).

**CONST_T §3.1 — B(4) = 43.95, B(8) = 1931.5. CONFIRMED**: B(4) ∈ [43.9486193106, 43.9486193107],
B(8) = B(4)² ∈ [1931.48113931, 1931.48113932] (tail Σ_{k>150} ≤ ln 2·152/2¹⁵⁰). Spot-check: §4.2's B(4a) column is
off mid-range (85 at q = 24; true 93.66, as STAR_CONST §9 and Codex QFIX found) — no decision depends on it.

**K33 / CONST_T §6.2 — "At q = 8 … C_T ≥ 1.27·10¹⁴ > 10¹³ whatever the local constants". Arithmetic CONFIRMED,
conclusion CONFIRMED a fortiori, one premise false.** √6·175.8·B(8)·½(36·486)² ∈ [1.273012, 1.273013]·10¹⁴ (r55k_1
A6; the C_1C_V threshold for the dominant term alone is 0.28027, CONST_T 0.2799 including the other terms). The
premise "C_V ≥ 1 is forced" is false in STAR_CONST's split reading (C_V^source = 0.072), but there the source base is
36·c_s·3 with c_s ≥ 319.198 > 486/3, so the bound only grows. Across schedules: with the sharp telescope (§1.2)
the q = 8 value is ≥ √6·64·B(8)·½(17496)² = 4.63·10¹³, and with any Stage-2 budget ≤ R/2 and R ≥ 62 the loose form
is ≥ 3.64·10¹³ (F ≥ 50.26, E4 below): **q = 8 is over 10¹³ on every schedule.**

**K26 — CONST_T §3.2 "optimised schedule … max F = 175.8 … gain 23×". REFUTED** (§1.1): inadmissible with Stage 1's
output ball; and "the max is what enters C_T" is false (§1.2). CONST_T also missed the free lever R_0: with the
exact telescope the sup over R is the asymptote 16/α², so neither the small-R peak nor d_min matters.

**CONST_T §2.5/§6.1 formula C_T = √6·F·B(4a)·Ĉ. CONFIRMED as an upper bound for q ≥ 8**, loose by F_max/(16/α²) (§1.2).

### STAR_CONST.md

**STAR_CONST Lemmas A1-A2 (D_1* is 3 covariant differences; the source term needs 𝒩_S(p) = {p, p+e_μ, p+e_ν} and
L(p), 2 per plaquette, reverse count 3). CONFIRMED (re-derived).** Collecting the coefficient of α_μ(y) in
⟨D_1α, v⟩ for the covariant curl gives D_1*v(y,μ) = Σ_{ν≠μ}[v_{μν}(y) − Ad⁻¹_{U(y−e_ν,ν)}v_{μν}(y−e_ν)] =
Σ_{ν≠μ}Ad⁻¹[∇_νv_{μν}(y−e_ν)]: three terms; the term (b,ν) touches the plaquette (y−e_ν; μν), of which b is the far
μ-link, and ∇_ν reaches only p and p + e_ν. Counting: 4V links × 3 = 6V plaquettes × 2. (I re-derived from the
standard covariant curl; I did not open SQ l.1383-1385.) This is the 486 → 3 that is worth 162× in the base.

**STAR_CONST (2′), (3′s), (4′) — spot-checked; one conservative slip.** (2′)'s C_δ = 8(2/δ_2 + 4) and (3′s)'s
C_A^s = 1/t + 2 + 4/s_0, C_B^s ≤ 20 re-derive. In (4′) the cut-off coefficient per edge is
4(β+1)²g² + 2g² ≤ (16β² + 2)g² ≤ 18β²g², ×8 (E3) = **144β², not 272β²** ("32β² + 2" should read 16β² + 2). The slip
is on the safe side: c_g = 8C_B^tot/κ + 144 = 5571.6 would be valid instead of 5699.6 (−2.2 %, ≈ −0.6 % in C_T(12),
−2 % at the plateau). Not used anywhere below.

**STAR_CONST §6.2/§7 — c_s = 411.92 (floor 319.20), c_g = 5699.63. CONFIRMED** as the arithmetic of its formulas:
T* = (√387 − 18)/4, c_s ∈ [411.9229708842, 411.9229708843], c_g ∈ [5699.632830341, 5699.632830342], floor
c_s(δ_2 = ρ = 0) ∈ [319.1979899, 319.1979900] (r55k_1 B1).

**K3 — "C_1 = 5699.6 computed while §8.3 quotes a figure computed at a supplied C_1 = 20. Which C_1 is it?"**
- **§8.3's C_T figures (9.8·10¹² at q = 11, 5.3·10¹² at q = 12, plateau 1.4·10¹²) are at C_1 = c_g = 5699.63.
  CONFIRMED as arithmetic** (r55k_1 B2: [9.811687, 9.811688]·10¹², [5.319981, 5.319982]·10¹², [1.401052, 1.401053]·10¹²
  with `sc1_cs.py`'s cut = 288(c_g + 18·3·c_s·32^{−2+8/q}) and A_cγ_c := 1). The control discriminates: C_1 = 20 in the
  same slot gives 3.959·10¹² at q = 12 (×1.344 off), so 5.3·10¹² cannot be a C_1 = 20 figure. They inherit K26.
- **The C_1 = 20 figure is "CONST_T's SUPPLIED reference value A_cγ_c = 236.9·C_1 = 4.7·10³ at C_1 = 20" and the
  conclusion drawn from it, "ε_* must be lowered by about a factor 2-10 below CONST_T's 10⁻⁴". REFUTED.** At
  C_1 = c_g the same expression is 1 350 243.0175 (×284.9816 in C_1; the "×287" of EPSSTAR l.218 / SESSION25 is
  1 350 243/4700 = 287.2857, a ratio against a prematurely rounded 4.7·10³ — agreeing with Codex DECADES F9), and EPSSTAR
  l.218's "1.348·10⁶" is itself mis-multiplied (r55k_1 B3a/B3b FAIL). More fundamentally ε_* = 10⁻⁴ violates Stage 1's
  own absorption inequality (EPSSTAR §3.2, confirmed below), so there was no 10⁻⁴ baseline; Theorem ES-1 supersedes
  the whole question.

### EPSSTAR.md

**K4 — Theorem ES-1: A_cγ_c ≤ (1 + √6)·C_{S1}(q, m)/m, "a bound containing NO c_K, c_RB, C_K′, C_B, c_N or ε_*"
(EPSSTAR §4.1). CONFIRMED (load-bearing step re-derived).** With 𝔞 := 9|N_3|c_Kε_*, 𝔟 := 9|N_3|^{1/2}|N_1|c_RBε_*²,
(ABS-ε) is 𝔞 + 𝔟 ≤ 1/(4m) (from 9|N_3|^{1/2}‖Φ‖_{ℓ²} ≤ 1/(4m), ‖M_3u‖_{ℓ²} ≤ |N_3|^{1/2}ε, ‖(M_1u)²‖_{ℓ²} ≤ |N_1|ε²).
The A_cγ_c bound is 36(1+√6)C_{S1}[c_K|N_3|ε_* + c_RB|N_3|^{3/4}|N_1|^{1/4}ε_*²] (from ‖M_3u‖_{ℓ⁴} ≤ |N_3|^{1/4}‖w‖_{ℓ⁴},
‖(M_1u)²‖_{ℓ⁴} ≤ ‖M_1u‖_∞‖M_1u‖_{ℓ⁴} ≤ ε|N_1|^{1/4}‖w‖_{ℓ⁴}, (5′), ‖w‖_{ℓ²(B_R)} ≤ (1+√6)ε_*). The first bracket term is
𝔞/9 exactly; the second is 𝔟·|N_3|^{1/4}/(9|N_1|^{3/4}) ≤ 𝔟/9 because |N_3| = 14 406 < |N_1|³ = 114 791 256 (exact).
Hence A_cγ_c ≤ 4(1+√6)C_{S1}(𝔞+𝔟) ≤ (1+√6)C_{S1}/m. *Slips that do not matter:* |N_3|^{3/4} = 343·6^{3/4} =
1314.9449 (EPSSTAR 1314.21), |N_3|^{1/4}/|N_1|^{3/4} = 0.1058421 (EPSSTAR 0.105889), |N_3|^{3/4}|N_1|^{1/4} = 6174
**exactly** (= 343·3·6; EPSSTAR 6171.3) (r55k_1 C1a/C1b FAIL, C1c PASS). *Scope caveat:* the bound controls V_c on
B_{3R/4−3}; combining it with F = 175.8 is K26.

**EPSSTAR §3.2 — "ε_* = 10⁻⁴ is not admissible at all". CONFIRMED.** (ABS-ε) at m = 1 caps
ε_* ≤ 1/(36·14 406·c_K) = 1.92822·10⁻⁶/c_K ≤ 2.824·10⁻⁸ at the smallest admissible c_K = 68.29.

**EPSSTAR §3.4/§4.2 — C_{S1}(12, 1) = 6963.995; A_cγ_c ≤ 2.402·10⁴ (m = 1), 2.871·10³ (m = 7), 0.99996 (m = 19 615).
CONFIRMED** (r55k_1 C2: [6963.994967, 6963.994968]; [24022.229, 24022.230]; [2871.2055, 2871.2056];
[0.99996098, 0.99996099]).

**K5 — "C_T = 5.29·10¹² at q = 12" (EPSSTAR §7.1, "C_T(q = 12) = 5.288·10¹², q_min = 11"). Arithmetic CONFIRMED;
as the constant of the stated construction REFUTED.** The harness reproduces [5.288348017, 5.288348018]·10¹² (r55k_1
C3) and the split 73.8 % / 0.00 % / 26.2 %. But F = 175.8 is inadmissible with EPSSTAR's own Stage-1 radii (K26).
Correct values for EPSSTAR's own radii: **2.0216·10¹³** in the file's own (loose) accounting — over 10¹³, and C_D(12)
= 1.549·10¹⁶ > 6.7·10¹⁵ — or **7.7008·10¹²** with the exact telescope exponent (§1.2). "q_min = 11" becomes
q* = 14.570 (loose) / 11.769 (sharp) against the real condition C_D ≤ 6.7·10¹⁵ at c_N = 2.

**K6 — EPSSTAR l.525 vs its own l.521 and requirement "η_♭ ≥ 4C_3ε_1² = 1.80·10⁻⁷⁸·C_3" (which is at l.523, not
l.527 as QFIX cites — l.527 begins "4. What it does and does not break"). CONFIRMED in substance; "exactly √10"
REFUTED literally.** From l.521's η_♭ = t_pr²/5.05·10⁹ and the l.523 requirement at ε_1 = 6.7·10⁻⁴⁰:
t_pr ≥ 2ε_1√(5.05·10⁹·C_3) ∈ [9.522489170, 9.522489171]·10⁻³⁵·√C_3 (9.5224022·10⁻³⁵ with the unrounded 640·53⁴ =
5 049 907 840). l.525 prints 3.01·10⁻³⁵: the ratio of printed numbers is [3.163617664, 3.163617665], not √10 =
3.162277660, but t_need/√10 = 3.011275·10⁻³⁵ rounds to exactly 3.01·10⁻³⁵, i.e. a factor 10 was lost under the root
(EPSSTAR's own l.524 "4.85 in ε_1" and l.780 "1.42·10⁵" are consistent with 9.52·10⁻³⁵). Corrected chain:
**C_D ≤ 1.7811920·10¹³/C_3^{1/4}** (not 3.17·10¹³); **C_T ≲ 1.97910·10¹⁰ − 3.56238·10¹⁰** with S4-16's frozen
(0.5-0.9)·10³, or **2.3248·10¹⁰ (c_N = 2) − 4.6496·10¹⁰ (c_N = 1)** with Λ(12) (QFIX §8.1, agreeing). Direction:
the repair bar is ×1.78 harder in C_D. No verdict changes. PROOF.md l.109 still prints "C_T ≲ 3.5e10".

**K27 — EPSSTAR l.608 "the floor over all δ-budgets is c_s ≥ 319.2, giving C_T ≥ 4.4·10¹² at q = 12". REFUTED as
a floor of this route.** (i) The stated reasoning does not give 4.4·10¹²: c_s → 319.198 with c_g held gives
[4.04325, 4.04326]·10¹² (0.1166 decades below 5.288·10¹², agreeing with QFIX §12.4) — and c_s → 319.2 needs
δ_2 → 0, where c_g → ∞, so it is not a floor at all. (ii) At fixed F = 175.8, R_0 = 64, q = 12 the best δ-budget on a
grid (ρ = 1/1000, δ_2 = 0.0715, T = 0.402) achieves **4.4359·10¹²** (r55k_2 P3; an upper bound on that restricted
minimum) — so "≈ 4.4·10¹²" happens to be the fixed-F optimum, by coincidence of the reasoning. (iii) The route as a
whole goes lower: consistent re-allocation (b) gives 3.158·10¹² (loose) / 2.506·10¹² (sharp) at q = 12, and the sharp
printed schedule 1.925·10¹². PROOF.md l.109 repeats the floor.

**EPSSTAR §6.4 — no-change floor ε_* ≥ 84·θ_0^SUP = 1.12·10⁻³⁷; "lowering ε_* is free, 21-25 decades". CONFIRMED,
with a currency caveat.** 84 × 1.3338·10⁻³⁹ = 1.1204·10⁻³⁷ at C_D = 0.9·10³·5.288·10¹². The floor is q- and
allocation-dependent (1.3127·10⁻³⁷ at q = 12 with Λ(12); 2.9141·10⁻³⁶ at q = 1000 — r55k_1 G5, agreeing with Codex),
but EPSSTAR's chosen ε_*(m = 19 615) ≥ 1.46·10⁻¹⁶ clears every version by ≥ 19 decades, so the conclusion stands. What
does NOT stand is QFIX's reuse of 1.12·10⁻³⁷ as "the" ε_* (K23).

**EPSSTAR §6.4 "τ_R = 2.75·10⁻¹⁵ is twenty-four decades larger than θ_0^SUP/C′ = 2.52·10⁻⁴¹". REFUTED (spot-check,
non-decisional):** log10(2.75·10⁻¹⁵/2.517·10⁻⁴¹) = 26.04 decades (half of TAUFLAT's 52.077 energy decades).

**EPSSTAR §6.6 — the η_♭ side-finding (52 decades; DESC-ε shortfall ≈ 9.7 decades). CONFIRMED** — see K7.

### TAUFLAT.md

**K7a — "the conflict is real" (TF1-A/B/C/D). CONFIRMED.** Window: τ_R ≤ θ_0^SUP/C′ ⟺ C_D ≤ (3.31·10⁷·53·2.75·10⁻¹⁵)^{−1/2}
∈ [455.2833009, 455.2833010] (exact 40000000000/192973 under the root). At C_D = 900·5.288·10¹²:
log10(η_A/η_B) ∈ [52.077008, 52.077009] (an η_♭ = energy-threshold log; the τ_♭ log is half, 26.0385 — Codex DECADES
F11, agreed), shortfall log10(4ε_1²/η_B) ∈ [9.707284, 9.707285] (4.854 in ε_1) (r55k_1 E1, E2). The two θ_0 are
distinct and both sit in τ_♭'s nested min (SQ l.318-319, l.1622, l.1633; quotes checked). *Currency:* 9.707 is at
q = 12 with the frozen (0.5-0.9)·10³ band and F = 175.8; it is 9.428 with Λ(12), 6.479 at the q-plateau (QFIX,
Codex), and **11.757 (loose) / 8.530 (b, loose) at q = 12 under consistent radii** — positive in every version.

**K7b — "LOAD-BEARING; (MS-Sob) and (SQ-dev) back on the critical path" (TAUFLAT §3.5, HANDOFF item 8). CONFIRMED as
a conditional ledger consequence.** The quotes it rests on exist verbatim: SQ.md l.1747 "PRICE-iii and DESC-ε have
their hypothesis (REG-min) discharged by §15.3"; HIST.md l.1323 "(MS-Sob) [OPEN; P]"; REVIEW_HIST_S4 l.50 "Theorem
AE-red: CONFIRMED as CONDITIONAL ⇐ (MS-Sob)." The numerical premise (DESC-ε (iii) fails) holds at the in-force
ε_1 = 6.7·10⁻⁴⁰ for every q ≥ 8, every δ-allocation, every radius split and either accounting under P-max (E4), so
option A cannot rescue it. It is reversible only by option C (lowering ε_1 — **not landed**: RLARGE.md contains no
"EPS1_EXEC" / "ε_1^cut" text) or by P-ct (OPEN). Status argument, not a proof: I confirm the ledger reading, not that
(MS-Sob) is the cheapest repair.

**TF1-E (EPSSTAR's three repair figures off by √10). CONFIRMED** (see K6).

**K8 — TAUFLAT §4 A "C_T has only 0.080 decades of room above that floor … buys only 0.160 decades of C_err".
Arithmetic CONFIRMED; as the route's room REFUTED; the decision (option A dead) CONFIRMED by a rigorous bound.**
log10(5.288/4.4) ∈ [0.079838, 0.079839] and EPS1_EXEC's log10(5.288/1.396) ∈ [0.578406, 0.578407] (r55k_1 E3). They
measure different things: 0.080 is the δ-budget room at fixed q = 12 against EPSSTAR's underived floor (K27; the
fixed-F grid optimum gives ≥ 0.0762); 0.578 is the q-lever 12 → 100 at a frozen allocation (QFIX §12.4's reading,
which I share). Neither is the route's room: allocation and the exact telescope move C_T(12) by a further
0.3-0.44 decades (§1.3). **Option A is nevertheless dead for every allocation (r55k_1 E4, PASS):** over every
δ-budget, every q ≥ 8 and every Stage-2 budget ≤ R/2 with R ≥ 62, Ĉ ≥ 54c_s + 288c_g ≥ min_w[P/(w(1−w)) + C/w] +
288·272 ≥ 5.17814·10⁵ (P = (√3888 + √36864)², C = 102 240, using c_s ≥ 8(9/T+2)/κ, c_g ≥ 8(16/δ_2+44)/κ + 272,
Cauchy-Schwarz in (T, δ_2) and convexity in w := 1 − T − δ_2) and F ≥ min_i 62^{2−Λ_i}(2Λ_i)^{Λ_i}2^{σ_i} ≥ 50.262
(Lemma S + S ≤ R/2), so C_T ≥ 1.2313·10¹¹ against the most lenient DESC-ε need C_T ≤ 6.6494·10¹⁰ (c_N = 1, q → ∞,
C_3 = 1, exact 640·53⁴): dead by ≥ 0.2676 decades. (The sharp-telescope liminf gives ≥ √6·64·B(8)·Ĉ_min = 1.57·10¹¹,
0.37 decades.) Under P-ct the same bound is 2.8·10⁹ and decides nothing.

*(Correction to the two paragraphs above, appended after `checks/r55k_4_out.txt` — criteria `r55k_4_criteria.md`
written first, report-only.)* In K7a read the consistent-radii shortfalls at q = 12 as **11.757 ((a) loose),
10.081 ((a) sharp), 8.532 ((b) loose), 8.131 ((b) sharp)** — "8.530" was a hand slip. In K8 read "move C_T(12) by a
further 0.3-0.44 decades" as: **relative to 5.288·10¹², the consistent constructions sit at +0.582 ((a) loose),
+0.163 ((a) sharp), −0.224 ((b) loose), −0.324 ((b) sharp) decades, and the inadmissible printed schedule with the
exact telescope at −0.439.** The sharp liminf bound is [1.56790, 1.56791]·10¹¹, 0.3725 decades above the most
lenient need (r55k_4 D2 PASS).

### EPS1_SWEEP.md

**K9 — "ε_1 IS SEVERAL SYMBOLS — at least FIVE" (§1). CONFIRMED as a lower bound; exact count NOT-VERIFIED.** Every
cited definition is where it is cited, with the quoted text: RLARGE l.58 (χ_Q cut), BFT_B l.3058
("ε_1 := [Λ_2(L²/(L²−1))(4C_eΛ_2 + 12c_h(Λ_2^{(1)})²Λ_2)]^{−1}·min(1, …)"), FLOW l.1927 ("On a disc |φ| ≤ ε_1 (fixed)"),
FLOW l.771 (mode amplitude), EXISTENCE l.2205 ("C = c_1^{ε_1}⋯c_ℓ^{ε_ℓ}"), HW l.1444 (ε_1^{gas}, superscripted).
EPS1_SWEEP lumps FLOW l.1927 (a disc radius in the Cartan variable φ) with FLOW l.2834 ("|q_αF| ≤ ε_1", a root-
projected flux bound); EPS1_EXEC §2.1 treats them as different objects. I did not read FLOW far enough to decide, so
the count is ≥ 5 and possibly 6 (the brief's "at least 6"). The scoping conclusion (option C touches only the χ_Q cut;
BFT_B's ε_1 is an O(1) formula) is CONFIRMED by the definitions.

**K11 — "a_RS's ceiling sits 15.62 decades BELOW DX′ … already today" (§4.3, (C2)). Arithmetic CONFIRMED; currency
stated.** RLARGE l.64 η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d)}, l.1020 a_RS := min{a_η, κε_1²/(256N)}, l.1026 "a_η taken
at its bare-level value η_1²/(2N)"; at N = 2, A_d = 9 the quadratic branches are active for ε_1 < 512 and
ε_1 < 814.6√κ, so a_RS = ε_1⁴/(4·9216²) **exactly** (not a fit). At **ε_1 = 6.7·10⁻⁴⁰ (RLARGE l.72's TB-1/rerun cell)**:
a_RS = 5.931360·10⁻¹⁶⁶, log10[(a_RS/10²)/(2.456·10⁻¹⁵²)] ∈ [−15.6171, −15.6170] (r55k_1 F1). Evaluated at the other
live values it is −15.114 (8.95·10⁻⁴⁰), −15.007 (9.52·10⁻⁴⁰), −14.506 (1.27·10⁻³⁹); with the c_RS = 5⁴ divisor −18.413
(Codex DECADES). The comparison is at C_Ω = c_+ = 1 and the bare /10². Whether a_RS is consumed at all is another
batch's question (PROOF [S25-fix 4] says it binds nothing on the live route).

**K10 — option C "SAFE WITH NAMED CONDITIONS (C1)-(C7)" (§5). NOT-VERIFIED as a whole; two conditions REFUTED, one
incomplete.** I did not re-run the 586-occurrence census. Of the conditions: (C1) scope — CONFIRMED by the definitions
(K9); (C2) arithmetic — CONFIRMED (K11; −35.03 = −15.617 − 19.415); **(C3) — REFUTED (sign inverted, K13)**;
**(C4) — REFUTED (its replacement value is above its own bound, K14)**; (C5) — prices CONFIRMED as 4Δ, 3Δ
(Δ = 4.853642787…), the ε_1^{−3} item stays ARGUED; (C6) — the four live values exist as cited (RLARGE l.71, l.72,
l.611; SF l.2837 / NORMS l.746) — CONFIRMED; **(C7) — incomplete**: the value being written is also a function of q,
C_3, (H2) (EPS1_EXEC §6.2, agreed) **and of the Stage-1/Stage-2 radius allocation** (K26), which moves the q = 12
requirement from 6.1·10⁻⁴⁵ to 5.8·10⁻⁴⁴ across the consistent constructions.

**EPS1_SWEEP §4.5 — "ε_1 ≤ √(η_♭/4) = 9.38495112638·10⁻⁴⁵ (exact to the digits shown; η_♭ = 3.52309230578·10⁻⁸⁸)".
REFUTED twice.** (i) The quoted value exceeds √(3.52309230578·10⁻⁸⁸/4) ∈ [9.384951126377803, …804]·10⁻⁴⁵ (r55k_1 F4a
FAIL; CTRL-2 9.38495112637·10⁻⁴⁵ PASSES). (ii) The 12-digit η_♭ is the exact image of TAUFLAT's 6-s.f. t_pr =
1.33384·10⁻³⁹ (`e1b_power.py` l.25, l.32: 3.523092305779·10⁻⁸⁸), not of the chain C_D = 900·5.288·10¹², which gives
3.523098101594·10⁻⁸⁸ (r55k_1 F7 FAIL; Codex DECADES F11 agrees) — the digits beyond the sixth are spurious.

**EPS1_SWEEP §2.2/§2.3 — "the ℓ¹ absorption margin is proportional to g/ε_1 and shrinks as ε_1 falls at fixed g";
"2m_*g/ε_1 … falls 4.854 decades". REFUTED** (K13).

### EPS1_EXEC.md

**K12 — (C6): "The four values are … a 2 × 2 table … that factorises exactly … The cell in force is ε_1 ≤ 6.7·10⁻⁴⁰"
(§1, header; P8 item 7). Conclusion CONFIRMED by reading; "exactly factorising" REFUTED; the gate has no
evidential power.** RLARGE l.70-72 reads "ε_1 ≤ min{9.52·10⁻⁴⁰ (TB-1: ≈ 6.7·10⁻⁴⁰), 1.13·10⁻¹⁸/C_Δ, 2.40·10⁻⁷/C_♭,
7.5·10⁻⁵r_♭, 2.04·10⁻⁹} … So ε_1 ≲ 6.7·10⁻⁴⁰ modulo the unevaluated C_Δ, C_♭, r_♭" — so 6.7·10⁻⁴⁰ is in force
**conditionally on C_Δ ≤ 1.69·10²¹, C_♭ ≤ 3.58·10³², r_♭ ≥ 8.9·10⁻³⁶** (RLARGE's own "modulo"). The cross-ratio
(1.2687·10⁻³⁹·6.7·10⁻⁴⁰)/(8.95·10⁻⁴⁰·9.52·10⁻⁴⁰) = 0.997639, not 1 (r55k_1 F2a FAIL); it is consistent with 1 only
within the printed rounding ([0.989083, 1.006215], F2b PASS). And the table factorises **by construction**:
REVIEW_SF_S7 l.47 ("lower it by a factor 0.7056, so ε_1 ≲ 8.95·10⁻⁴⁰") and l.53 ("9.52·10⁻⁴⁰ (×0.7056 by TB-1 →
6.7·10⁻⁴⁰)") produced the TB-1 cells by multiplying, and l.251's "slightly worse (×0.75)" is the ratio of the two
computed class cells (9.52/12.687 = 0.7504). EPS1_EXEC's "Neither factor was read from the cell it predicts … so this
is not a tautology" is therefore false: the gate can fail only on a transcription error (defect 3). EPS1_EXEC's own
§8.2 concedes the in-force cell was decided by reading, which is the part I confirm.

**K13 — "(C3) has its sign inverted" (§3.3). CONFIRMED.** PLD l.994-995 (quoted text checked): "(SG^{net}) … holds at
t = ε_1/(σ_*²g²) iff v ≤ σ_*²g² + 2m_*σ_*²g³/ε_1. Hence no Gaussian model whose aligned variance exceeds
σ_*²g²(1 + 2m_*g/ε_1) satisfies (SG^{net})". At fixed g, 2m_*g/ε_1 ∝ 1/ε_1 rises by ×7.139088·10⁴ (4.853642787
decades) when ε_1 goes 6.7·10⁻⁴⁰ → 9.38495·10⁻⁴⁵ (r55k_1 F3), so the admissible set grows and the clause is easier;
what shrinks is the asserted t-range 0 ≤ t ≤ ε_1/(σ_*²g_k²) (PLD l.984). Codex DECADES F11 agrees.

**K14 — "EPS1_SWEEP §4.5's recommended 9.38495112638·10⁻⁴⁵ sits 2.3406·10⁻¹³ ABOVE [its bound]" (§4.3). CONFIRMED**:
relative excess ∈ [2.34059, 2.34060]·10⁻¹³ (r55k_1 F4b).

**EPS1_EXEC §4.6 / patch P1 — "ε_1^cut ≤ 9.38·10⁻⁴⁵ … admissible at every precision at which η_♭ is published".
REFUTED as an unconditional statement.** It is admissible against the three published η_♭ roundings, all of which
inherit F = 175.8 (K26). Under EPSSTAR's own Stage-1 radii the q = 12 requirement is ≤ 6.106·10⁻⁴⁵ (exact telescope)
or ≤ 8.861·10⁻⁴⁶ (file's accounting): 9.38·10⁻⁴⁵ fails DESC-ε (iii) in both. It is safe under allocation (b)
(≤ 3.63·10⁻⁴⁴ / 5.76·10⁻⁴⁴). P1's condition list (i)-(v) must gain "(vi) the Stage-1/Stage-2 radius split", or the
number must be dropped in favour of the parametric form P1 already carries. Its *method* (truncate a square-root
ceiling down; carry the parametric form) is right.

**EPS1_EXEC §4.4 q-table, row q = 8: "≥ 1.27·10¹⁴ … 1.627·10⁻⁴⁷ … −2.761". REFUTED.** The row substitutes CONST_T's
q = 8 floor (C_1C_V = 1, multiplicity 486) as an equality into a table built from EPSSTAR's M-sharp/P-max harness, in
which C_T(8) ∈ [8.24514, 8.24515]·10¹⁴ and the shift is −4.386 decades, not −2.761 (r55k_1 F6; Codex DECADES F11 agrees).
The table as a whole also freezes Λ at q = 8 (QFIX §8.2) and inherits K26.

**EPS1_EXEC §4.5 — "Over q, the room is 0.578 decades of C_T". Arithmetic CONFIRMED** (K8); it is the q-lever, not
room above a floor (QFIX §12.4's reading, which I share).

**EPS1_EXEC §5 — (C5) prices 19.4146 / 9.7073 / 14.5609. CONFIRMED** as 4Δ, 2Δ, 3Δ with Δ ∈ [4.853642787,
4.853642788] (r55k_1 F5). The a_RS power 4 is exact from RLARGE's definitions (K11). The ε_1^{−3} Cauchy item stays
ARGUED (HIST l.864 gives the method, not the constant), as EPS1_EXEC says.

### QFIX.md

**K15 — "q was never chosen on the merits" (§4). CONFIRMED (provenance, by reading).** SQ.md l.1622 Theorem EPS-0:
"Fix q := 8." with no optimisation recorded; EPSSTAR §7.1 (l.545-555) reports q = 12 as the first q under the 10¹³
proxy in both m-columns of a satisfiability sweep.

**K16a — "Thirteen consumers pull one way; exactly one pulls the other" (§2, 14 rows). REFUTED as a census.** Under
the adopted P-max convention row 2 (B(4a)) is q-independent; rows 13-14 are domain floors, not consumers; rows 7-10
are one mechanism (C_D) counted four times; and **row 4 (A_cγ_c) reverses**: d/dϑ log[(1−ϑ)(4ϑ)^{ϑ/(1−ϑ)}X^{1/(1−ϑ)}]
= log(4Xϑ)/(1−ϑ)², X = 27c_s, so the bound decreases in q only for q < 16X = 432c_s ∈ [177950.723421, 177950.723422]
and rises after (r55k_1 G6: 0.981400872752 at q = 177 950 → 0.981400875456 at 10⁶ → 0.981400877535 at 10⁷). Agreeing
with Codex QFIX F03. *In substance* nothing in the practical range opposes raising q except θ_G — the effect of the
reversal on C_T is ~10⁻⁹ relative.

**K16b — "There is no upper constraint anywhere in the mathematics" (§3.1 box; §10 PROVEN list). REFUTED unscoped;
CONFIRMED scoped to the Moser step.** The EPS-T step works for every q > 4 (with c′_ϑ ≤ 1 for q ≥ 8). But
t_pr = C′τ_♭ ≤ C′τ_R ≤ θ_0^{SQ4} ≤ θ_G(q) = 1.168·10⁻¹²/q (SQ l.318-319, l.1622, l.1633; θ_G from EPS-0b-avg's
"qβ ≤ ½", SQ l.1608-1610), so the chain is capped where θ_G(q) = θ_0^SUP: **q ≈ 2.12887·10²⁵** at the plateau C_D
(r55k_1 G7; Codex QFIX F04/DECADES F4 agree), and the objective → −∞ as q → ∞. Astronomically far, but the universal
claim and the "endpoint q → ∞ optimum" are false.

**QFIX §10 "PROVEN: C_T(q) is strictly decreasing with a finite positive plateau". REFUTED as a global statement**
(Codex F03's asymptotic argument, which I re-derived: f(ϑ) = X + Xϑ log ϑ + O(ϑ) enters C_T with a positive
coefficient, so C_T approaches its limit from below eventually), **true on every practical range**: C_T(q) − C_T(∞) is
+8.353·10⁵ at q = 10⁶, +0.8353 at 10¹², +8.353·10⁻¹⁹ at 10³⁰ (r55k_1; 10⁶⁰ is beyond my precision).

**K17 — "q ≥ 12 … q = 11 fails by ×1.16" (§3.2). CONFIRMED in QFIX's model; "lowest admissible q is 12" REFUTED over
the reals; model-dependent.** Λ(q) = 4·2^{2+4/q}(4.94 + 3.34·32^{1/q}) ⇒ Λ(8) = 228.332906, Λ(12) = 189.459168,
Λ(∞) = 132.48 (exact); C_D(11) = 7.74385·10¹⁵ = 1.15579 × 6.7·10¹⁵; C_D(12) = 4.05178·10¹⁵ (r55k_1 G1-G2). But
q = 11.5 already passes (5.42173·10¹⁵) and the real threshold is **q* ∈ [11.19115, 11.19116]** (Codex F12 agrees).
The threshold moves with the radius allocation: 14.570 / 11.769 (EPSSTAR's radii, loose / sharp), 10.569 / 10.333
((b)), 10.086 (printed, sharp). It exists only at the **unlowered** ε_1 = 6.7·10⁻⁴⁰: once ε_1 := ε_1^cut(q), the linear
clause ε_1 < t_pr holds at every q by ×142 125.

**K18 — "a_RS ∝ C_D^{−8}" (§5.1). CONFIRMED as conditional algebra:** ε_1^cut = t_pr/(2√(5.05·10⁹C_3)) ∝ C_D^{−2} on the
θ_0^SUP branch, and a_RS ∝ ε_1⁴ exactly on RLARGE's bare-level branch (K11; stronger than QFIX's five-row fit, which
Codex F06 rightly calls a fit). Conditional on ε_1 being set to ε_1^cut, on θ_0^SUP binding (K16b), and on a_RS being
the live exponent (other batch); with KN-step's linear η_1 or a quadratic live exponent the power is −4.

**K19 — "total lever 24.089 decades" (§5.2). CONFIRMED as arithmetic; currency conditional.** obj(∞) − obj(8) ∈
[24.089105, 24.089106] (r55k_1 G3; Codex 24.089105770869); 24.0891 / 24.0920 under consistent allocations (a) / (b),
loose or sharp (r55k_2, r55k_3) — so the lever, unlike the absolute numbers, survives K26. Its currency is the
hypothetical a_RS-ceiling margin (8 × decades of C_D); in ε_1^cut decades it is 6.022276, in a quadratic live
exponent 12.0446 (Codex F10). QFIX §10's "recovers 24.089 of the 19.415 decades" mixes baselines (Codex F11, agreed).

**K20 — "argmax q = 1000" (§5.3, §7.1). REFUTED as an argmax; CONFIRMED as the output of QFIX's pre-registered rule.**
obj is strictly increasing on QFIX's own grid (obj(10⁴) − obj(1000) = +0.014984, obj(10⁶) − obj(1000) = +0.016626;
r55k_1 G8 FAIL, CTRL-5 PASS). The rule "smallest grid point within 0.05 decades of the supremum" selects 1000 (QFIX
says so in §5.3 itself); restoring θ_G moves the true supremum to q ~ 10²⁵ without changing its value to 3 decimals.

**K21 — "ε_1 ≤ 3.8·10⁻⁴³ at q = 1000, c_N = 2, C_3 = 1 … 3.5·10⁻⁴³ at q = 100" (§7.2). Arithmetic CONFIRMED for
q = 1000; q = 100 REFUTED; the target as a whole REFUTED as unconditional.** ε_1^cut(1000) ∈ [3.8234580, 3.8234581]·10⁻⁴³
and 3.8·10⁻⁴³ is below it (G4a/b PASS). **ε_1^cut(100) ∈ [3.4950274, 3.4950275]·10⁻⁴³, so the quoted 3.5·10⁻⁴³ is above
its own ceiling; the two-figure value is 3.4·10⁻⁴³** (G4c FAIL; Codex DECADES F5 agrees). And the 3.8·10⁻⁴³ holds only
if (i) ε_* ≥ 2.9141·10⁻³⁶ is chosen (K23), and (ii) the radius allocation has α ≳ 0.3: under EPSSTAR's own radii the
q = 1000 requirement is 1.803·10⁻⁴³ (exact telescope) / 2.616·10⁻⁴⁴ (file's accounting), which 3.8·10⁻⁴³ violates
(§1.3).

**K22 — "S4-16's 'C_D ≈ (0.5−0.9)·10³·C_T' is exactly 2.022·Λ(8)·c_N over c_N ∈ [1,2]" (§8.2). CONFIRMED in substance,
"exactly" REFUTED.** REVIEW_SQ_S4 l.370-374 (text checked) evaluates A_0 = c_NC_T′(2.47N√κ_+ + 32^{1/8}C_0) at
"c_N ∈ [1, 2]" and q = 8 and rounds to "(0.5-0.9)·10³". Exactly, C_D/C_T = 2.022·Λ(8)·c_N + 93.6/C_T =
461.689·c_N + 93.6/C_T; the rounded band does not contain 461.69 (Codex QFIX F08 agrees). The band's width is c_N and
its level is a q = 8 evaluation — QFIX's point stands.

**K23 — Codex DECADES' q = 1000 cutoff 1.4695·10⁻⁴⁴ vs QFIX's 3.8235·10⁻⁴³. RECONCILED; both correct for their
inputs; QFIX's text is internally inconsistent.** QFIX's chain sets t_pr = θ_0^SUP(q) alone; its own checker fixes
`EPSSTAR_FLOOR = D("1.12e-37")` (`checks/qf1b_q.py` l.60) and its text quotes ε_* = 1.12·10⁻³⁷ (§2 item 2, §5.4,
§12.3). At that ε_*, θ_ε(1000) = 1.12·10⁻³⁷/(16·3.34·32^{1/1000}) ∈ [2.088557, 2.088558]·10⁻³⁹ < θ_0^SUP(1000) ∈
[5.434154, 5.434155]·10⁻³⁸, so t_pr ≤ θ_ε binds and ε_1^cut ≤ [1.469503, 1.469504]·10⁻⁴⁴ — Codex's number (r55k_1 G5).
To keep 3.8235·10⁻⁴³ one must take **ε_* ≥ [2.914094, 2.914095]·10⁻³⁶** (the q = 1000 no-change floor), which is
admissible: EPSSTAR's ε_*(m = 19 615) ≥ 1.46·10⁻¹⁶. So QFIX's value is right once ε_* is stated correctly; the
1.12·10⁻³⁷ it carries is EPSSTAR's q = 12, frozen-Λ floor, stale at every q ≠ 12.

**QFIX §5.4/§12.3 — "θ_G does not become the binding entry of θ_0^{SQ4} until q > 5.573·10²⁶". Arithmetic
reproduces (G7: [5.57302, 5.57303]·10²⁶); REFUTED as the relevant threshold.** It compares θ_G with θ_ε at the stale
ε_* = 1.12·10⁻³⁷; the chain is affected only when θ_G(q) < θ_0^SUP(q), at q ≈ 2.12887·10²⁵. At EPSSTAR's actual
ε_* (≥ 1.46·10⁻¹⁶) θ_G does become the min of θ_0^{SQ4} already at q ~ 50-4·10⁵ — harmlessly, since both stay far
above θ_0^SUP.

**QFIX §8.1 — "EPSSTAR l.525 is inconsistent … by √10". CONFIRMED in substance** (K6); "exactly √10" is literally
false (3.163618 vs 3.162278) and the "l.527" citation should be l.523.

**QFIX §8.2 — Λ(12)/Λ(8) = 0.82975, Λ(8)/Λ(∞) = 1.72353; C_D(12) = 4.052·10¹⁵; ε_1^cut(12) = 1.295·10⁻⁴⁴; TAUFLAT's
9.707 → 9.428. CONFIRMED** in QFIX's model (G1-G4; Codex DECADES F5 for 9.428). All inherit K26.
*(Appended note: the "q ~ 50-4·10⁵" in the last-but-two paragraph is a hand estimate — θ_G(q) = θ_ε(q) at
ε_* = 1.44·10⁻¹² gives q ≈ 47, at ε_* = 1.462·10⁻¹⁶ q ≈ 4.3·10⁵ — not an interval-checked figure.)*

---

## 3. The Codex gpt-6-astra/max reviews: what I used, and whether I agree

Both files were read as they are on disk at 22:51Z. **CODEX_REVIEW_QFIX.md** (559 lines) is complete — it ends with a
"Final source receipt" (22:21:58Z) and a stdout summary; it was 380 lines when the lead listed it. **CODEX_REVIEW_DECADES.md**
(670 lines) is complete — "Completion receipt: 2026-10-28 22:25:13 UTC" and an 80-row final table; it was 142 lines when
listed. Neither ends mid-thought now.

| Codex finding | my verdict | basis |
|---|---|---|
| QFIX F01 (original QF1-3 gate impossible: ϑ ≤ ½ fails at q = 5, 6) | **AGREE** | QFIX l.76 text; K2 |
| QFIX F02 (first script squares t_pr) | AGREE (not independently re-run; QFIX §9.1 discloses it) | — |
| QFIX F03 (A_cγ_c reverses at q = 432c_s; C_T not globally strictly decreasing) | **AGREE** | derivative re-derived; r55k_1 G6 |
| QFIX F04 (θ_G / nested minima omitted; objective → −∞; stale ε_* floor; 1.4695·10⁻⁴⁴) | **AGREE** | K16b, K23; r55k_1 G5, G7 |
| QFIX F05 (input-gate q-dependence; census not exhaustive) | **AGREE in conclusion, PARTLY in reasoning**: the input-gate dependence is the θ_G mechanism already in QFIX's row 12 (EPS-0b-avg verifies EPS-T's 𝒮 hypothesis through qβ ≤ ½, SQ l.1608-1611), so it is not an independent second consumer; the census is refuted by F03 alone | SQ l.1608-1627 |
| QFIX F06 (a_RS ∝ ε_1⁴ only fit-verified) | **AGREE about QFIX's check; DISAGREE that the power is NOT-VERIFIED** — it is exact from RLARGE l.64/l.1020/l.1026's bare-level definitions (EPS1_EXEC §5.1 and I re-derived it); its live relevance is another batch's | K11, K18 |
| QFIX F07 (objective rows reproduce) | **AGREE** | r55k_1 G3 |
| QFIX F08 (√10 and band corrections: substance yes, "exactly" no) | **AGREE** | K6, K22 |
| QFIX F09 (gates cannot decide global claims) | AGREE for QF1-2, -5, -6, -7 (from Codex's description of the code; I did not re-read qf1_q.py line by line) | — |
| QFIX F10 (a_RS consumption NOT-VERIFIED; 12.0446 for a quadratic live exponent) | **AGREE** | lever/2 = 12.0446 |
| QFIX F11 (mixed baselines; stale 0.9; 1.038 → 1.037) | AGREE (did not recompute 6.4567 or 1.0375) | — |
| QFIX F12 (q = 11.5 passes) | **AGREE** | r55k_1 G2c; real q* = 11.19115 |
| DECADES F3 (24.089 is not live currency; ×4 not ×8 for a quadratic exponent) | **AGREE** | K19 |
| DECADES F4 (θ_G; fixed ε_* gives 1.4695·10⁻⁴⁴ and lowering ≥ 4.6589; need ε_* ≥ 2.9141·10⁻³⁶) | **AGREE** — and it is the reconciliation the lead asked for (K23) | r55k_1 G5 |
| DECADES F5 (13.14 not 13.15; 3.5·10⁻⁴³ above its ceiling; 2.037 changes the endpoint) | AGREE (3.5·10⁻⁴³ re-derived, G4c; 13.1436 = 8·log10 B(4) re-derived by hand from B(8) = B(4)²) | — |
| DECADES F9 (×287 is not the C_1 factor: 284.98; 287.29 vs rounded 4700; ×1.78 and ×1.16 confirmed) | **AGREE** | r55k_1 B3, C5, G2 |
| DECADES F11 (Δ-multiples; PLD sign; 36.63/31.78; 9.38495112638e-45 above bound; η_♭ chain 3.523098·10⁻⁸⁸; 0.080 vs 0.578 different endpoints; −2.761 uses a lower bound; 52 decades is an energy log) | **AGREE** on every item I recomputed (F3-F7, E2, E3) | r55k_1 |
| DECADES F12 rows on qf1/ee1 gates | AGREE | — |

**Two things neither Codex review found, both decisional:** K26 (F = 175.8 is inadmissible with Stage 1's output
ball) and §1.2 (CONST_T §2.5's Ĉ^{Σ1/p_i} ≤ Ĉ makes the formula loose by exactly F_max/(16/α²)). Together they make
the EPS1_EXEC and QFIX ε_1 targets unsafe under the only Stage-1 radii any file states. Codex reproduced the printed
q-chain to 12 digits — which is exactly what an inherited modelling error survives.

---

## 4. Every figure I re-derived, with its correct value and its currency

(Interval endpoints from `checks/r55k_1_out.txt` unless marked r55k_2/3/4. "frozen" = S4-16's (0.5-0.9)·10³ band, i.e.
Λ at q = 8; "printed" = F = 175.8, R_0 = 64, m = 19 615, |𝒩_S| = 3, P-max; c_N = 2 and C_3 = C_Ω = c_+ = 1 unless stated.)

| figure (file) | quoted | re-derived | verdict | currency |
|---|---|---|---|---|
| ϑ ≤ ½ for every q > 4 (CONST_T l.307) | true | ϑ = 4/q ≤ ½ ⟺ q ≥ 8 | REFUTED | exact |
| c_ϑ ≤ 1 for every q > 4 (CONST_T §2.4(e)) | true | c_ϑ ≤ 1 ⟺ q ≥ [5.175261, 5.175262]; c_ϑ(5) = 1.31072 | REFUTED | λ = 1/(2ϑ) |
| two-potential constant c′_ϑ (not in the batch) | — | ≤ 1 ⟺ q ≥ 8, = 1 at q = 8 | new | λ = 1/(4ϑ) |
| B(4), B(8) (CONST_T §3.1) | 43.95, 1931.5 | 43.94861931, 1931.481139 | CONFIRMED | Π(p_i−1)^{m/p_i} |
| q = 8 floor (CONST_T §6.2) | 1.27·10¹⁴ | 1.273012·10¹⁴ | CONFIRMED | C_1C_V = 1, 486, F = 175.8, loose |
| same, over all schedules | — | ≥ 3.64·10¹³ (loose, F ≥ 50.26); 4.63·10¹³ (sharp) | conclusion holds | any Stage-2 budget ≤ R/2 |
| C_1C_V threshold at q = 8 (CONST_T) | 0.2799 | 0.28027 (dominant term only) | consistent | — |
| F_max optimised (CONST_T §3.2) | 175.8 @ R = 79 | 175.80281 @ 79 | arithmetic CONFIRMED, **inadmissible** | budget R/2 − 4 |
| F_max with Stage 2 ⊂ B_{3R/4−3} | — | **672.02797 @ 155** | new | EPSSTAR's Stage-1 radii |
| F asymptote / sharp sup | "max enters C_T" | sup = 16/α² (64, 256, 83.59) | REFUTED (loose by 2.75, 2.63, 1.26) | exact telescope exponent |
| c_s, c_g (STAR_CONST §7) | 411.92, 5699.63 | 411.9229708842…, 5699.632830341… | CONFIRMED | δ_2 = ρ = 1/16 |
| c_s floor (STAR_CONST) | 319.20 | 319.1979899 | CONFIRMED | δ_2 = ρ = 0 |
| (4′) cut-off coefficient (STAR_CONST §5) | 272β² | 144β² suffices | slip (safe side) | per edge ×8 |
| C_T(11/12/100) (STAR_CONST §8.3) | 9.8/5.3/1.4 ·10¹²| 9.811687/5.319981/1.401052 ·10¹² | CONFIRMED (arithmetic) | C_1 = c_g, A_cγ_c := 1, R_0 = 32, printed F |
| same with C_1 = 20 in the cut slot (control) | — | 3.959484·10¹² at q = 12 | shows §8.3 is at c_g | — |
| 236.9·C_1 at C_1 = c_g (EPSSTAR l.218) | 1.348·10⁶ | 1 350 243.0175 | REFUTED | CONST_T's c_c = 50, ε_* = 10⁻⁴ |
| "×287" (EPSSTAR, SESSION25) | 287 | C_1 ratio 284.98164; vs rounded 4700: 287.28575 | REFUTED as C_1 factor | — |
| "factor 2-10" drop in ε_* (STAR_CONST §8.3) | 2-10 | meaningless: ε_* = 10⁻⁴ inadmissible | REFUTED | — |
| ε_* cap at m = 1 (EPSSTAR §3.2) | 1.9282·10⁻⁶/c_K | 1/(36·14 406·c_K) = 1.92822·10⁻⁶/c_K | CONFIRMED | (ABS-ε) |
| \|N_3\|^{3/4}; ratio; \|N_3\|^{3/4}\|N_1\|^{1/4} (EPSSTAR) | 1314.21; 0.105889; 6171.3 | 1314.9449; 0.1058421; 6174 exactly | slips, harmless | — |
| C_{S1}(12,1) (EPSSTAR) | 6963.995 | 6963.994967 | CONFIRMED | 4096·c_g |
| A_cγ_c bounds m = 1/7/19 615 | 2.402e4/2.871e3/0.99996 | 24022.23/2871.206/0.999961 | CONFIRMED | q = 12 |
| C_T(12) (EPSSTAR §7.1) | 5.288·10¹² | 5.288348017·10¹² | arithmetic CONFIRMED; construction REFUTED | printed |
| C_T(12), consistent | — | 2.0216·10¹³ (a, loose); 7.7008·10¹² (a, sharp); 3.1576·10¹² / 2.5062·10¹² (b) | new | r55k_2 / r55k_3 |
| t_pr needed (EPSSTAR l.525) | 3.01·10⁻³⁵√C_3 | 9.522489170·10⁻³⁵√C_3 (9.5224022·10⁻³⁵ with 640·53⁴) | REFUTED | ε_1 = 6.7·10⁻⁴⁰ |
| ratio to "√10" | exactly √10 | 3.163617664 vs 3.162277660 | REFUTED literally | — |
| C_D ceiling (EPSSTAR l.525) | 3.17·10¹³ | 1.7811920·10¹³/C_3^{1/4} | REFUTED | — |
| C_T ceiling (EPSSTAR l.525/l.701, PROOF l.109) | 3.5-6.3·10¹⁰ | 1.97910-3.56238·10¹⁰ (frozen); 2.3248-4.6496·10¹⁰ (Λ(12), c_N = 2/1) | REFUTED | q = 12 |
| C_T floor (EPSSTAR l.608, PROOF l.109) | ≥ 4.4·10¹² | not a floor; c_s-only 4.04325·10¹²; fixed-F grid 4.4359·10¹² | REFUTED | — |
| no-change floor (EPSSTAR §6.4) | 1.12·10⁻³⁷ | 1.1204·10⁻³⁷ (q = 12 frozen); 1.3127·10⁻³⁷ (Λ(12)); 2.9141·10⁻³⁶ (q = 1000) | CONFIRMED with currency | θ_ε divisor 16·3.34·32^{1/q} |
| τ_R vs θ_0^SUP/C′ (EPSSTAR §6.4) | 24 decades | 26.04 | REFUTED (minor) | — |
| C_D window (TAUFLAT TF1-C) | 455.283301 | 455.2833009-…010 | CONFIRMED | τ_R = 2.75·10⁻¹⁵, C′ = 53 |
| η_A/η_B (TAUFLAT TF1-B) | 52.077 | 52.077008-…009 | CONFIRMED | C_D = 900·5.288·10¹²; an energy log |
| shortfall (TAUFLAT TF1-D) | 9.707 | 9.707284-…285 | CONFIRMED | q = 12 frozen, printed |
| shortfall, other currencies | — | 9.428 (Λ(12)); 6.479 (plateau); 11.757/10.081 (a); 8.532/8.131 (b) | — | r55k_4 |
| "0.080 decades of room" (TAUFLAT §4 A) | 0.080 | 0.079838 (arithmetic) | arithmetic CONFIRMED; as room REFUTED | fixed q, underived floor |
| "0.578 over q" (EPS1_EXEC §4.5) | 0.578 | 0.578406 | CONFIRMED (it is the q-lever) | q 12 → 100, frozen |
| option A lower bound (new) | — | C_T ≥ 1.2313·10¹¹ (loose) / 1.5679·10¹¹ (sharp) vs need ≤ 6.6494·10¹⁰ | option A dead CONFIRMED | P-max, any allocation |
| a_RS(6.7·10⁻⁴⁰) (EPS1_SWEEP, ARS_FIX) | 5.93136·10⁻¹⁶⁶ | 5.931360·10⁻¹⁶⁶ (exact rational) | CONFIRMED | N = 2, A_d = 9 |
| a_RS margin vs DX′ (EPS1_SWEEP §4.3) | −15.62 | −15.6171…−15.6170 | CONFIRMED | ε_1 = 6.7·10⁻⁴⁰, bare /10² |
| same at 8.95e-40 / 9.52e-40 / 1.27e-39 | — | −15.114 / −15.007 / −14.506 | — | other live values |
| Δ = log10(6.7e-40/9.38495112638e-45) | 4.853643 | 4.853642787-…788 | CONFIRMED | — |
| 2Δ/3Δ/4Δ (EPS1_EXEC §5) | 9.707/14.561/19.415 | 9.707285/14.560928/19.414571 | CONFIRMED | — |
| 2×2 cross-ratio (EPS1_EXEC §1.3) | "exactly" 1 | 0.997639 (printed-rounding range [0.98908, 1.00622]) | REFUTED literally | — |
| g/ε_1 change (PLD l.995; EPS1_SWEEP vs EPS1_EXEC) | falls 4.854 / rises 4.854 | rises ×71 390.88 = 4.853643 decades | EPS1_EXEC CONFIRMED | fixed g |
| √(η_♭/4) (EPS1_SWEEP §4.5) | 9.38495112638·10⁻⁴⁵ | 9.384951126377803·10⁻⁴⁵ | quoted value REFUTED | η_♭ = 3.52309230578·10⁻⁸⁸ |
| excess (EPS1_EXEC §4.3) | 2.3406·10⁻¹³ | 2.34059-2.34060·10⁻¹³ | CONFIRMED | relative |
| 12-digit η_♭ (EPS1_SWEEP) | 3.52309230578·10⁻⁸⁸ | chain 3.523098101594·10⁻⁸⁸; from t_pr = 1.33384e-39: 3.523092305779·10⁻⁸⁸ | REFUTED as "exact" | — |
| EPS1_EXEC q = 8 row | −2.761 | −4.3858…−4.3857 (C_T(8) = 8.24514·10¹⁴) | REFUTED | same harness |
| ε_1^cut(12) target (EPS1_EXEC P1) | 9.38·10⁻⁴⁵ | 1.2948·10⁻⁴⁴ (QFIX model); 6.106·10⁻⁴⁵ / 8.861·10⁻⁴⁶ (a); 5.765·10⁻⁴⁴ / 3.632·10⁻⁴⁴ (b) | REFUTED as unconditional | allocation |
| Λ(8), Λ(12), Λ(∞) (QFIX §8.2) | 228.333, 189.459, 132.48 | 228.332906, 189.459168, 132.48 | CONFIRMED | — |
| C_D(11)/6.7·10¹⁵ (QFIX §3.2) | ×1.16 | 1.15579-1.15580 | CONFIRMED | printed, c_N = 2 |
| lowest admissible q (QFIX) | 12 | real q* = 11.19115 (printed); 14.570/11.769 (a); 10.569/10.333 (b) | REFUTED over reals | unlowered ε_1 |
| lever (QFIX §5.2) | 24.089 | 24.089105-…106; 24.0891/24.0920 consistent | CONFIRMED | a_RS margin currency |
| obj(8)/(12)/(100)/(1000)/(∞) | −52.664/−34.473/−28.748/−28.592/−28.575 | −52.66401/−34.47256/−28.74757/−28.59155/−28.57490 | CONFIRMED | printed |
| argmax (QFIX §5.3) | q = 1000 | grid argmax 10⁶; obj increasing | REFUTED as argmax | — |
| ε_1^cut(1000) (QFIX §7.2) | 3.8·10⁻⁴³ | 3.8234580·10⁻⁴³ (printed); 1.803·10⁻⁴³ (a, sharp) | value CONFIRMED in model; target REFUTED unconditional | ε_* ≥ 2.914·10⁻³⁶ needed |
| ε_1^cut(100) (QFIX §7.2) | 3.5·10⁻⁴³ | 3.4950274·10⁻⁴³ | REFUTED (use 3.4·10⁻⁴³) | printed |
| q=1000 cutoff with θ_ε at ε_* = 1.12e-37 (Codex) | 1.4695·10⁻⁴⁴ | 1.469503-…504·10⁻⁴⁴ | CONFIRMED | stale ε_* |
| θ_G crossing (QFIX §5.4) | 5.573·10²⁶ | 5.57302·10²⁶ (vs θ_ε at stale ε_*); relevant: 2.12887·10²⁵ (vs θ_0^SUP) | REFUTED as relevant | — |
| A_cγ_c reversal (Codex F03) | 432c_s | 177 950.723421… | CONFIRMED | m = 19 615 |

---

## 5. Summary table — every claim reviewed, with its verdict

| # | file | claim (locating string) | verdict |
|---|---|---|---|
| 1 | CONST_T | "q = 8 is the worst admissible choice" (§8.1, §9 E4) | **REFUTED** — C_T ↓ in q on (4,∞); worst only on [8,∞) |
| 2 | CONST_T | "all hold for every q > 4" (l.307-308) | **REFUTED** — ϑ ≤ ½ ⟺ q ≥ 8; c_ϑ ≤ 1 ⟺ q ≥ 5.175261; two-potential c′ ≤ 1 ⟺ q ≥ 8 |
| 3 | CONST_T | exact scale-invariance for every σ > 2 (§2.4(f)) | CONFIRMED |
| 4 | CONST_T | B(4) = 43.95, B(8) = 1931.5 (§3.1) | CONFIRMED |
| 5 | CONST_T | q = 8: C_T ≥ 1.27·10¹⁴ > 10¹³ (§6.2) | CONFIRMED (≥ 3.6·10¹³ on every schedule) |
| 6 | CONST_T | "C_1C_V ≥ 1 is forced" (§6.1) | **REFUTED** (C_V^source = 0.072 in the split reading; STAR_CONST §6.3 already says so) |
| 7 | CONST_T | optimised F = 175.8, "the max is what enters C_T" (§3.2) | **REFUTED** — inadmissible with Stage 1's ball (672.03 admissible); sharp sup is 16/α² |
| 8 | CONST_T | C_T = √6·F·B(4a)·Ĉ (§2.5, §6.1) | CONFIRMED as an upper bound for q ≥ 8 (loose by F_max·α²/16) |
| 9 | STAR_CONST | Lemmas A1-A2 (3 differences; 𝒩_S, L(p), 2/3 counts) | CONFIRMED |
| 10 | STAR_CONST | (2′), (3′s) constants | CONFIRMED (spot-check) |
| 11 | STAR_CONST | (4′) "272β² … FORCED" | **REFUTED** — 144β² suffices (safe-side slip; c_g could be 5571.6) |
| 12 | STAR_CONST | c_s = 411.92 (floor 319.20), c_g = 5699.63 | CONFIRMED |
| 13 | STAR_CONST | §8.3 C_T ≤ 9.8·10¹² (q=11), 5.3·10¹² (q=12), 1.4·10¹² plateau | CONFIRMED as arithmetic, at C_1 = c_g (inherits #7) |
| 14 | STAR_CONST | §8.3 "ε_* must be lowered by about a factor 2-10" | **REFUTED** |
| 15 | EPSSTAR | "1.348·10⁶ … 287× larger" (l.218, l.711) | **REFUTED** — 1 350 243.0; C_1 factor 284.98 |
| 16 | EPSSTAR | Theorem ES-1, A_cγ_c ≤ (1+√6)C_{S1}/m, constant-free | CONFIRMED |
| 17 | EPSSTAR | ε_* = 10⁻⁴ not admissible (§3.2) | CONFIRMED |
| 18 | EPSSTAR | C_{S1}(12,1) = 6963.995; A_cγ_c table (§3.4, §4.2) | CONFIRMED |
| 19 | EPSSTAR | C_T(q = 12) = 5.288·10¹² (§7.1) | **REFUTED** as the construction's constant (arithmetic CONFIRMED) — 2.02·10¹³ / 7.70·10¹² with its own Stage-1 radii |
| 20 | EPSSTAR | q_min = 11 (l.555) | **REFUTED** — real-condition q* = 11.19 (printed), 11.77-14.57 (own radii) |
| 21 | EPSSTAR | l.525: t_pr ≥ 3.01·10⁻³⁵, C_D ≤ 3.17·10¹³, C_T ≲ 3.5-6.3·10¹⁰ | **REFUTED** — 9.52·10⁻³⁵, 1.78·10¹³, 1.98-3.56·10¹⁰ |
| 22 | EPSSTAR | l.608 floor C_T ≥ 4.4·10¹² | **REFUTED** |
| 23 | EPSSTAR | no-change floor 1.12·10⁻³⁷; lowering ε_* free (§6.4) | CONFIRMED (floor is q-dependent; conclusion holds) |
| 24 | EPSSTAR | "τ_R … twenty-four decades larger" (§6.4) | **REFUTED** — 26.04 (minor) |
| 25 | EPSSTAR/TAUFLAT | 52.077 decades; C_D ≤ 455.283301; shortfall 9.707 | CONFIRMED |
| 26 | TAUFLAT | LOAD-BEARING; (MS-Sob)/(SQ-dev) back on the critical path (§3.5) | CONFIRMED (conditional on ε_1 = 6.7·10⁻⁴⁰ in force and P-max) |
| 27 | TAUFLAT | TF1-E: EPSSTAR's repair figures off by √10 | CONFIRMED |
| 28 | TAUFLAT | "only 0.080 decades of room" (§4 A) | **REFUTED** as the route's room (arithmetic CONFIRMED) |
| 29 | TAUFLAT | option A (sharpen C_T) DEAD | CONFIRMED (rigorous: C_T ≥ 1.23·10¹¹ vs ≤ 6.65·10¹⁰) |
| 30 | EPS1_SWEEP | ε_1 is at least five symbols (§1) | CONFIRMED (as a lower bound) |
| 31 | EPS1_SWEEP | option C SAFE WITH NAMED CONDITIONS (C1)-(C7) (§5) | NOT-VERIFIED (census not re-run; (C3), (C4) wrong; (C7) incomplete) |
| 32 | EPS1_SWEEP | a_RS ceiling 15.62 decades below DX′ today (§4.3) | CONFIRMED (arithmetic at ε_1 = 6.7·10⁻⁴⁰) |
| 33 | EPS1_SWEEP | ℓ¹ margin 2m_*g/ε_1 "shrinks"/"falls 4.854" (§2.2-2.3) | **REFUTED** — rises 4.8536 decades |
| 34 | EPS1_SWEEP | 9.38495112638·10⁻⁴⁵ "exact to the digits shown" (§4.5) | **REFUTED** — above its bound by 2.34·10⁻¹³ |
| 35 | EPS1_SWEEP | η_♭ = 3.52309230578·10⁻⁸⁸ (12 digits) | **REFUTED** as exact — spurious beyond 6 s.f. |
| 36 | EPS1_EXEC | (C6): 6.7·10⁻⁴⁰ is the cell in force | CONFIRMED (modulo C_Δ ≤ 1.69·10²¹, C_♭ ≤ 3.58·10³², r_♭ ≥ 8.9·10⁻³⁶) |
| 37 | EPS1_EXEC | 2×2 table "factorises exactly … not a tautology" (§1.3) | **REFUTED** — cross-ratio 0.997639; cells built by multiplication |
| 38 | EPS1_EXEC | (C3) sign inverted (§3.3) | CONFIRMED |
| 39 | EPS1_EXEC | EPS1_SWEEP's value 2.3406·10⁻¹³ above its bound (§4.3) | CONFIRMED |
| 40 | EPS1_EXEC | P1: ε_1^cut ≤ 9.38·10⁻⁴⁵ admissible at every precision (§4.6) | **REFUTED** as unconditional — fails under EPSSTAR's own radii (needs ≤ 6.11·10⁻⁴⁵) |
| 41 | EPS1_EXEC | q-table row q = 8: −2.761 (§4.4) | **REFUTED** — −4.386 in the same harness |
| 42 | EPS1_EXEC | "room is 0.578 decades over q" (§4.5) | CONFIRMED (it is the q-lever) |
| 43 | EPS1_EXEC | (C5) prices 19.415 / 9.707 / 14.561 (§5) | CONFIRMED (ε_1^{−3} item stays ARGUED) |
| 44 | QFIX | q never chosen on the merits (§4) | CONFIRMED |
| 45 | QFIX | 14 consumers, 13 want q large (§2) | **REFUTED** — row 4 reverses at q > 177 950.72; rows 2, 13-14 not consumers; 7-10 one mechanism |
| 46 | QFIX | no upper constraint anywhere (§3.1, §10) | **REFUTED** unscoped (θ_G caps at q ≈ 2.13·10²⁵); CONFIRMED for the Moser step |
| 47 | QFIX | C_T(q) strictly decreasing, PROVEN (§10) | **REFUTED** globally (true through q = 10³⁰) |
| 48 | QFIX | q = 11 fails by ×1.16 (§3.2) | CONFIRMED (×1.15579, printed model, c_N = 2) |
| 49 | QFIX | lowest admissible q is 12 (§3.2) | **REFUTED** — q* = 11.19115; q = 11.5 passes |
| 50 | QFIX | a_RS ∝ C_D^{−8} (§5.1) | CONFIRMED (conditional algebra; power 4 exact from RLARGE) |
| 51 | QFIX | total lever 24.089 (§5.2) | CONFIRMED (arithmetic; allocation-independent; currency conditional) |
| 52 | QFIX | argmax q = 1000 (§5.3) | **REFUTED** as an argmax (rule output only) |
| 53 | QFIX | target ε_1 ≤ 3.8·10⁻⁴³ (§7.2) | **REFUTED** as unconditional (value 3.8235·10⁻⁴³ CONFIRMED in-model) |
| 54 | QFIX | 3.5·10⁻⁴³ at q = 100 (§7.2) | **REFUTED** — ceiling 3.4950·10⁻⁴³ |
| 55 | QFIX | (0.5-0.9)·10³ band is c_N at q = 8 (§8.2) | CONFIRMED in substance ("exactly" overstated) |
| 56 | QFIX | EPSSTAR l.525 off by √10 (§8.1) | CONFIRMED in substance ("exactly √10" false; l.527 → l.523) |
| 57 | QFIX | θ_G binds only for q > 5.573·10²⁶ (§5.4, §12.3) | **REFUTED** as the relevant threshold (2.13·10²⁵ vs θ_0^SUP) |
| 58 | QFIX | Λ(q) values; prefactor frozen at q = 8 (QF1-4) | CONFIRMED |
| 59 | Codex vs QFIX | 1.4695·10⁻⁴⁴ vs 3.8235·10⁻⁴³ at q = 1000 | CONFIRMED both — they differ by ε_* (1.12·10⁻³⁷ vs ≥ 2.914·10⁻³⁶) |
| 60 | TAUFLAT | §4 B C_err-prefactor lever (×71 391; 1.433 decades; ≈1.7 short) | NOT-VERIFIED (not checked) |
| 61 | STAR_CONST | §8.2 "(★) exactly as written fails at every q" (M-lit/P-max) | NOT-VERIFIED (not checked) |
| 62 | EPS1_SWEEP | §2 consumer census / classification (586 occurrences) | NOT-VERIFIED (not re-run) |
| 63 | EPS1_SWEEP | §3.2 "nothing breaks; paid entirely in g" | NOT-VERIFIED (not checked; wrap levels 183.6 → 204.0 spot-checked by hand) |
| 64 | EPSSTAR | §6.1 four distinct ε_* | NOT-VERIFIED (one occurrence spot-checked: RLARGE l.70's 2.476·10⁻¹³/C_Δ) |

**Counts: 32 CONFIRMED, 6 NOT-VERIFIED, 26 REFUTED** (rows 1-64; row 59 counts as CONFIRMED). Hand-only spot checks
not counted: EPSSTAR §4.3's ×1.8571 = (171366/14406)^{1/4} ✓; EPS1_SWEEP's wrap levels log_3(2n_H) 183.6 → 204.0 ✓.

**Count correction (appended; the line above was written before a row-by-row recount):** **31 CONFIRMED** (rows 3, 4,
5, 8, 9, 10, 12, 13, 16, 17, 18, 23, 25, 26, 27, 29, 30, 32, 36, 38, 39, 42, 43, 44, 48, 50, 51, 55, 56, 58, 59),
**6 NOT-VERIFIED** (31, 60, 61, 62, 63, 64), **27 REFUTED** (1, 2, 6, 7, 11, 14, 15, 19, 20, 21, 22, 24, 28, 33, 34, 35,
37, 40, 41, 45, 46, 47, 49, 52, 53, 54, 57). Total 64.

---

## 6. For the lead

### 6.1 Every REFUTED item, with its correction

1. CONST_T/HANDOFF "q = 8 is the worst admissible choice" → *C_T decreases in q on (4, ∞); q = 8 is the worst choice
   in [8, ∞); on (4, 8) CONST_T's constants fail and the route is worse.*
2. CONST_T "all hold for every q > 4" → *ϑ ≤ ½ ⟺ q ≥ 8; c_ϑ ≤ 1 ⟺ q ≥ 5.175261; with two potentials the needed
   quarter-split constant c′_ϑ ≤ 1 ⟺ q ≥ 8, so the formula is valid exactly on q ≥ 8.*
3. CONST_T "C_1C_V ≥ 1 forced" → *only the product c_s ≥ 319.2 is forced; C_V^source = 0.072* (STAR_CONST §6.3).
4. **CONST_T optimised F = 175.8 (budget R/2 − 4) → inadmissible: Stage 2 must live inside Stage 1's output ball
   B_{3R/4−3} (SQ l.1496; EPSSTAR §3.1); admissible max F = 672.03 with EPSSTAR's Stage-1 radii, 105.32 with a Stage-1
   gap R/16 − 4 (R_0 = 256). With the exact telescope exponent Ĉ^{1−2^{−i_*}} the sup over R is the asymptote
   16/α² (256 and 83.59), so "the max is what enters C_T" is false.**
5. STAR_CONST (4′) "272β², forced" → *144β² suffices* (safe side; c_g 5699.6 → 5571.6 possible).
6. STAR_CONST §8.3 "ε_* must be lowered by about a factor 2-10" → *meaningless: ε_* = 10⁻⁴ violates (ABS-ε); use
   Theorem ES-1.*
7. EPSSTAR l.218/l.711 "1.348·10⁶ (×287)" → *1 350 243.0; ×284.98 in C_1; 287.29 only against the rounded 4.7·10³.*
8. **EPSSTAR "C_T(q = 12) = 5.288·10¹²" → *arithmetic right, construction inconsistent; with EPSSTAR's own Stage-1
   radii 2.0216·10¹³ (file's accounting) or 7.7008·10¹² (exact telescope).***
9. EPSSTAR "q_min = 11" → *real condition C_D ≤ 6.7·10¹⁵ at c_N = 2: q* = 11.19115 (printed), 11.769 / 14.570 (own
   radii, sharp / loose), 10.33-10.57 (re-allocated).*
10. EPSSTAR l.525 → *t_pr ≥ 9.5225·10⁻³⁵√C_3, C_D ≤ 1.7812·10¹³/C_3^{1/4}, C_T ≲ 1.98-3.56·10¹⁰ (frozen band) or
    2.32-4.65·10¹⁰ (Λ(12)).*
11. EPSSTAR l.608 "floor C_T ≥ 4.4·10¹²" → *not a floor; the c_s argument gives 4.04·10¹²; the fixed-F δ-optimum is
    ≈ 4.436·10¹²; consistent re-allocations reach 2.5-3.2·10¹².*
12. EPSSTAR "twenty-four decades" → *26.04.*
13. TAUFLAT "only 0.080 decades of room" → *0.080 is fixed-q δ-budget room against an underived floor; the route's
    C_T(12) spans −0.44 to +0.58 decades across consistent constructions; option A is dead anyway (rigorous bound).*
14. EPS1_SWEEP (C3) "2m_*g/ε_1 shrinks / falls 4.854" → *rises 4.8536 decades; what shrinks is PLD l.984's t-range.*
15. EPS1_SWEEP §4.5 "9.38495112638·10⁻⁴⁵ (exact)" → *above its bound by 2.34·10⁻¹³ relative; truncate: 9.38495112637·10⁻⁴⁵.*
16. EPS1_SWEEP's 12-digit η_♭ → *exact only for the 6-s.f. t_pr; the chain value is 3.523098101594·10⁻⁸⁸.*
17. EPS1_EXEC "2×2 table factorises exactly … not a tautology" → *cross-ratio 0.997639; the TB-1 cells were made by
    multiplying by 0.7056 (REVIEW_SF_S7 l.47, l.53) and ×0.75 is the ratio of the computed class cells (l.251); the
    gate cannot fail except on transcription.*
18. **EPS1_EXEC P1 "ε_1^cut ≤ 9.38·10⁻⁴⁵ … admissible at every precision" → *admissible only on the inadmissible
    F = 175.8; under EPSSTAR's own Stage-1 radii the q = 12 requirement is ≤ 6.106·10⁻⁴⁵ (exact telescope) /
    8.861·10⁻⁴⁶ (file's accounting), so 9.38·10⁻⁴⁵ violates DESC-ε (iii). Add the radius split to P1's conditions or
    land only the parametric form.***
19. EPS1_EXEC q-table q = 8 "−2.761" → *−4.386 (C_T(8) = 8.245·10¹⁴ in the same harness).*
20. QFIX "13 of 14 consumers want q large" → *row 4 reverses at q > 432c_s = 177 950.72; row 2 is q-free under P-max;
    rows 13-14 are domain floors; rows 7-10 are one mechanism.*
21. QFIX "no upper constraint anywhere" → *none in the Moser step; θ_G(q) = 1.168·10⁻¹²/q caps t_pr at q ≈ 2.13·10²⁵.*
22. QFIX "C_T(q) strictly decreasing (PROVEN)" → *decreasing through q = 10³⁰ at least; eventually approaches its limit
    from below (Codex F03).*
23. QFIX "lowest admissible q is 12" → *q* = 11.19115 over the reals (q = 11.5 passes); only at the unlowered ε_1.*
24. QFIX "argmax q = 1000" → *obj increases on the whole grid; 1000 is the pre-registered rule's pick.*
25. **QFIX "ε_1 ≤ 3.8·10⁻⁴³ at q = 1000" → *holds in QFIX's model only with ε_* ≥ 2.914·10⁻³⁶ (not the 1.12·10⁻³⁷ it
    quotes) and on the inadmissible F; under EPSSTAR's own radii the requirement is ≤ 1.803·10⁻⁴³ (exact telescope)
    / 2.616·10⁻⁴⁴ (file's accounting).***
26. QFIX "3.5·10⁻⁴³ at q = 100" → *3.4·10⁻⁴³ (ceiling 3.4950·10⁻⁴³).*
27. QFIX "θ_G binds only for q > 5.573·10²⁶" → *that compares θ_G with θ_ε at a stale ε_*; the chain-relevant crossing
    θ_G = θ_0^SUP is at q ≈ 2.12887·10²⁵.*

### 6.2 What changes in PROOF.md's tally or HANDOFF's critical path

- **Tally: no count changes from this batch** — nothing in it is a counted ledger item; every C_T / ε_1 figure is a
  number inside CONDITIONAL items. The changes are to numbers and to one prerequisite.
- **New prerequisite on the critical path, ahead of landing T55-B (EPS1_EXEC's ε_1 patch) and T55-N (QFIX's q):**
  fix the Stage-1/Stage-2 split of the radius budget in SQ §15.1 (a stated Stage-1 output radius ρ, Stage 2 confined
  to B_{ρ−3}), and replace CONST_T §2.5's Ĉ by Ĉ^{1−2^{−i_*}} (equivalently F_max by 16/α²). Until then no absolute
  C_T(q), q_min or ε_1^cut in the chain is established — only q-ratios (the 24.089 lever survives).
- **Do not land EPS1_EXEC's P1 number 9.38·10⁻⁴⁵ or QFIX's 3.8·10⁻⁴³ as written.** Under the only Stage-1 radii any
  file states they violate the clause they were built to satisfy (by ×1.54 and ×2.11 in ε_1). Land the parametric
  form ε_1^cut = t_pr/(142125√C_3), t_pr = 1/(3.31·10⁷C_D²), C_D = 2(1.011c_NΛ(q)C_T(q, α) + 46.8), with α named.
- **HANDOFF item 8: keep "(MS-Sob)/(SQ-dev) back on the critical path" (CONFIRMED) and keep "(A) sharpening C_T is
  DEAD", but replace the reason "0.080 decades of room against 4.854 needed"** by the rigorous bound: under P-max,
  over every δ-allocation, q ≥ 8, R_0 ≥ 62 and Stage-2 budget ≤ R/2, C_T ≥ 1.23·10¹¹ (1.57·10¹¹ with the exact
  telescope) against the most lenient need C_T ≤ 6.65·10¹⁰ (c_N = 1, q → ∞, C_3 = 1). Option A revives only under
  P-ct. Its "(C) lower ε_1 … to ≤ 9.38e-45" needs the allocation caveat above.
- **HANDOFF item 4 and closing paragraph:** "q = 8 is the worst admissible choice" → "C_T decreases with q; q = 8 is
  the worst choice in [8, ∞)". Item 4's "(CONST-T): expand C_1 and C_V" is done (STAR_CONST) and superseded by the
  prerequisite above.
- **PROOF.md l.109 ([S24-flag 3])**: "would need C_T ≲ 3.5e10, below this route's own floor (c_s ≥ 319.2 ⟹ C_T ≥
  4.4e12)" → "would need C_T ≲ 2.0-3.6e10 (frozen band; 2.3-4.6e10 with Λ(12)); option A is dead by a rigorous lower
  bound C_T ≥ 1.2e11 over every allocation (P-max)". The "4.4e12 floor" should not be quoted.
- **PROOF.md l.6917-6920 (item 3, (CLS-min))**: "at q = 8 … C_T ≥ 1.27e14: provably over. At q ≈ 30 it is under" —
  both halves survive every consistent construction (q = 8 ≥ 3.6·10¹³; q = 32 ≤ 5.6·10¹² even in the worst one).
- **SESSION25_RESULTS / SYMBOLS:** "×287 on C_1" → ×285; "52-decade τ_♭ error" → 52 decades of η_♭ (26 of τ_♭).

### 6.3 Codex verdicts used
Agree with QFIX F01, F03, F04, F07, F08, F10, F12 and DECADES F3, F4, F5 (3.5·10⁻⁴³), F9, F11 on every item I
recomputed; agree with QFIX F02, F09, F11 without recomputing; agree with QFIX F05's conclusion but not its framing
(the input-gate dependence is θ_G, already QFIX's row 12); **disagree with QFIX F06 on one point**: a_RS ∝ ε_1⁴ is
exact from RLARGE l.64/l.1020/l.1026 (bare-level value), not merely a fit — its live relevance is the other batch's.
Neither Codex review found K26 or the telescope looseness (§1); both reproduced the printed chain, which carries them.

*(End of REVIEW55_CONST.md. Files written by this reviewer: this file; checks/r55k_1_criteria.md, r55k_1_const.py,
r55k_1_out.txt, r55k_1_err.txt, r55k_1_run1_abort_out.txt, r55k_1_run1_abort_err.txt; r55k_2_criteria.md,
r55k_2_posthoc.py, r55k_2_out.txt, r55k_2_err.txt, r55k_2_run1_abort_out.txt, r55k_2_run1_abort_err.txt;
r55k_3_criteria.md, r55k_3_sharp.py, r55k_3_out.txt, r55k_3_err.txt; r55k_4_criteria.md, r55k_4_display.py,
r55k_4_out.txt, r55k_4_err.txt. No git command was run.)*

*(Two precision notes, appended after re-reading.)* (1) §6.2 "Option A revives only under P-ct" should read "**can**
revive only under P-ct": my P-ct bound (2.8·10⁹) decides nothing, and QFIX §6's P-ct clearance (×1.034 at q ≳ 1000,
c_N = 2) is computed on the printed F. (2) §1.1's "no-change floor ≤ 2.93·10⁻³⁶" is the printed chain's q = 1000 value;
under allocation (b) or the exact telescope C_D is smaller and the floor rises to ≈ 10⁻³⁵ (hand estimate: ≈ 8·10⁻³⁶
for (b)-loose, ≈ 2·10⁻³⁵ for printed-sharp at q → ∞) — still ≥ 18 decades below the ε_* those constructions use. In
§1.3 item 3 read the (b) margins as ×2.77 (loose) / ×3.49 (sharp).
*(Last correction, appended: in §1.1's table the asymptote for budget R·(1/2 − 1/128) − 3 is 16/(63/128)² = 66.05,
not 66.08 — a hand slip in a display column; the max-F column is the computed one.)*
