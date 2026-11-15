Reviewer model: claude-opus-5-5

# REVIEW55_TENT — Opus 5.5 re-review of batch C7 (TENTQ / YSUP / FACEB / GESIGN / COFUN)

UTC at start: 2026-10-28T22:13:29Z
Check-id prefix: r55t_ . Deliverable is append-only; no git; this is the only file written in $L
(criteria/scripts go under $L/checks/r55t_* as the brief requires, and nowhere else in the repo).

## PRE-STATED (written before any derivation; statements only)

Targets, with what would count as a refutation of each. "Refute" below means I exhibit the correct
statement/value and its derivation; failure to settle is NOT-VERIFIED, never CONFIRMED.

T1 TENTQ
 T1a "box charges eliminated". Refuted if the elimination step uses an identity that fails on the
     stated configuration class (a box-charge term survives), or if it eliminates them only under a
     hypothesis not available at that point.
 T1b "(NEUT-box) is false ... by a clean power", struck. The refutation is itself refuted if: the
     counter-family is not admissible for the statement as banked (wrong class / wrong norm / wrong
     quantifier); the claimed power is miscounted (the ratio is bounded uniformly); or the object
     refuted is not the banked (NEUT-box) (symbol/name collision). Confirmed only if I rebuild the
     counter-family and its power myself.

T2 YSUP
 T2a "the averaging does not beat the core". Refuted by an explicit averaging gain (a factor that
     tends to 0 with n) on the class the claim covers.
 T2b "(TENT-osc) false by n^2". Refuted if the exponent is not 2, if the witness is inadmissible, or
     if the statement refuted differs from the banked (TENT-osc).
 T2c Normalisation erratum at YSUP ~l.249 (mixed normalisations; Codex mixed ratio 486/65).
     Refuted if the mixed ratio is not 486/65 or if the normalisations are in fact consistent.

T3 FACEB
 T3a face (b) = (TENT-osc) with n = L^k, square on neither leg. Refuted if the identification
     needs a square on a leg, or n is not L^k, or face (b) as stated in the BFT source differs.
 T3b FB-CLASS: witness u = (1/8) d*delta_p, constant 65/26244. Refuted if the exact constant
     differs; separately I settle whether the decimal 2.4768e-3 is rounded in the wrong direction
     (65/26244 = ? to 5 significant figures, exact rational comparison).
 T3c FB-NOEST. T3d FB-LOCAL and the ratio 243/260 (exact recomputation).
 T3e FB-BOOT "no lower bound at all" versus Codex's M >= (2/3) max(A - B, 0). FB-BOOT is refuted
     if Codex's bound holds with no sign hypothesis on the objects as FACEB defines them.
 T3f "dimensionless => k-independent" versus Codex's Phi_k(d delta_c)(c) = 3^{-4k} - 1. Refuted if
     a dimensionless quantity in FACEB's setting is exhibited with genuine k-dependence.

T4 GESIGN
 T4a Proposition GS-ZERO (r = infinity, chi == 1, G' = h_p constant, kernel G_e == 0). Vacuous if
     Lemma LD does NOT admit r = infinity, or if Y^p DOES depend on r (so the r = infinity value is
     not the object the sign question is about). Refuted if G_e is not identically 0 there.
 T4b GS-WINDOW. T4c "the circularity does not close" (base step free because K'_0 = 0 exactly at
     BFT_A ~l.2761): refuted if K'_0 != 0 at the cited place, or if the induction needs more than
     the base step. T4d FB-ONE-LEG upgraded to PROVEN: refuted if its load-bearing step fails or
     rests on an unproven item.

T5 COFUN
 T5a "target was stale" (session-9 text already decided in session 10). Refuted if the session-10
     decision is not in the source, or decides a different statement.
 T5b three classes share the name (CO-fun); one is FALSE as stated and is the class D1 uses.
     Refuted if fewer/more classes, or the false one is not D1's, or it is not false.
 T5c Lemma CO-pin (PROVEN-HERE), and the relocation to coarse size 0.3462 * n^3 * max|Q_X|.
     Refuted if the load-bearing step fails or the constant is wrong (exact recomputation).
 T5d handle norms 1/3 and 8/3, "3x sharper": refuted if either norm or the sharpening factor is
     miscomputed.
 T5e universal negative "no per-level sharpening can remove the k-factor": refuted by a per-level
     scheme that removes it; NOT-VERIFIED if the quantifier ("every per-level sharpening") is not
     actually discharged by the argument given.
 T5f Codex COFUN tail: CO-pin does not establish that the gauge-side obstruction has disappeared
     or that RS10-6 is discharged. I adjudicate agree/disagree with reasons.

Systemic checks applied to every claim: (i) symbol collisions (verify by file:line which object
each symbol is); (ii) stale minima/quantifiers; (iii) whether each gate/check could have failed.

### PRE-STATED addendum (appended after READING the five files, both Codex reviews and the cited
### BFT_A/BFT_B/LINEAR_PACKAGE ranges; before any derivation, criteria file or script)

Reading done so far (no derivation): TENTQ, YSUP, FACEB, GESIGN, COFUN in full; CODEX_REVIEW_FACEB in
full; CODEX_REVIEW_COFUN as on disk at 22:17:51Z (28586 bytes, ends at F14); BFT_A l.18-47, 440-500,
598-612, 885-900, 1684-1722, 1864-1935, 2752-2815, 2970-2992, 2590-2600, 3388-3399, 3503-3580;
BFT_B l.3575, 3586-3590, 3796-3834, 3955-3967, 3976-3991, 4033-4040, 4104-4132, 4180-4205;
LINEAR_PACKAGE l.64-80, 120-130, 166-172; REVIEW_BFT_A_S8 l.240-262; REVIEW_BFT_B_S9_S10 l.551-600,
895-902. While reading I formed three suspicions; the targets below that bear on them carry NO
pre-registration weight beyond the label and are marked (c).

T6 (c) SYMBOL COLLISION on h_l. LINEAR_PACKAGE §1.2 defines the slice functional ORDER-AVERAGED
   (avg over the 4! coordinate orders and y in B(X)); BFT_B §27.1/§29.2 describe it with ONE fixed
   coordinate order, and COFUN §3 rebuilds that one. Test: exact h_0 kernel max|c| and l1 row sum for
   both operators at d = 4, L = 3. Refutes COFUN's "sharp 1/3" as a statement about the lane's h if
   the order-averaged max differs from 1/3; changes the exact funnel constants (65/26244, 243/260) if
   the fixed-order funnel differs from the order-averaged one.
T7 (c) GS-BASE's "(CC-0) holds exactly" at x_0 = 0. Refuted (or downgraded to NOT-VERIFIED) if the
   cited identities (Lemma CD; Xi^T N_B = 0) hold only as functionals on Lambda_* / Lambda_0, i.e.
   give (cc) and leave the level-k ROOT values of D(first source) uncontrolled.
T8 (c) GS-ONELEG's upgrade of FB-ONE-LEG to PROVEN. Refuted if Lemma RC and Proposition COF-res are
   not two pieces of one decomposition of one quantity for one source class (different sources,
   different comparison objects).
T9 Codex FACEB R1-R11 and Codex COFUN F1-F14: each verdict I use will be adjudicated agree/disagree.
Numeric verdicts: only from exact Fraction arithmetic in checks/r55t_*; criteria file first.


---

## 0. Check record r55t (criteria -> script -> output), and what each clause could decide

Files: `checks/r55t_criteria.md` (stat 22:34:58Z, BEFORE the script), `checks/r55t_checks.py`,
`checks/r55t_out.txt`, `checks/r55t_err.txt` (only /usr/bin/time's report). Run 22:37:38-22:37:40Z,
2.0 s, 134 MB peak, python3 -I, nice 10, thread vars = 1, Fractions/ints only. One run; no criterion
edited; nothing post-hoc. Built from SOURCE definitions (BFT_A l.599, l.1872; LINEAR_PACKAGE §1.2;
BFT_B l.2024); none of tq1/ys1/fb1/gs1/cf1/rev8 was read or run.

| clause | result | what it can decide |
|---|---|---|
| A1 witness funnel, ORDER-AVERAGED h, k=2 | PASS: phi_1 = -1/432, phi_2 = -17/104976, Phi_2 = -65/26244 | independent rebuild of S8-7/YSUP/FACEB's rationals from the S4' definition; A6 shows it can fail |
| A2 termination k = 3, 4 | PASS: phi_3 = phi_4 = 0 exactly, Phi_3 = Phi_4 = -65/26244 | YSUP's "terminates"; k <= 4 only (Codex FACEB R2 gives the all-k argument) |
| A3 Phi_k(d delta_c)(c) | PASS: -80/81, -6560/6561, -531440/531441 = 3^{-4k} - 1 | decides "dimensionless => k-free": it is k-DEPENDENT |
| A4 h_0 kernel, both operators | sum|c| = 8/3 for both (PASS); max|c| = **10/81 order-averaged vs 1/3 fixed order** | **T6 collision is REAL** |
| A5 witness with the FIXED-ORDER h (order 0123) | phi_1 = -1/72, phi_2 = 0, **Phi_2 = Phi_3 = -1/72** | the exact witness constants are operator-dependent |
| A6 designed-FAIL controls | FIRED: corner roots give Phi = 17/1296; un-normalised u gives -130/6561 | shows A1 can fail |
| A7 h_0(d lambda) = mean - root value; Q_str d = d A | PASS, both operators | implementation cross-check (not a reviewed claim) |
| B1 ||d chi^5||_1 = 2d n^{d-1} | PASS: d=2 k=1,2,3 (12, 36, 108); d=4 k=1,2 (216, 5832) | TENTQ §2.2(a) |
| B2 box sum <chi^5, d*j0> (different code path) | PASS: equals B1 exactly in all five cases | Proposition QSBP on the extremal configuration |
| B3 ||D||_inf = 2d | PASS (4 in d=2, 8 in d=4) | tq1b's "= 2d" |
| B4 NEUT-box ratio with D_perp, d = 4 | PASS: **R = 104/9 (n=3), 2912/27 (n=9)** >= n^2 - 1 | QFALSE; exact R = (2d n^{d-1} - 2d)/(6n) since ||D_perp||_inf = 6 |
| B5 partition of unity | PASS | sanity |
| B6 designed-FAIL (tent scale n-1) | FIRED: TV 64 vs 216 | shows B1 can fail |
| C1 Codex R1's 2x2 example | PASS: y = (0, 2) | pointwise lower bound can vanish at eps = 1/2 |
| C2 M >= (A-B)/(1+eps), M <= (A+B)/(1-eps), 200 exact instances | PASS | guards my algebra for the sup lower bound |
| C3 scalar G = -1/2 | PASS: y = (2/3)a | the 2/3 is sharp |
| D1 0.0024768 vs 65/26244 | PASS: difference = 89/2050312500 > 0 | the decimal OVERSTATES the lower bound |
| D2 ratios | PASS: 243/260 (common normalisation), 486/65 (YSUP l.249's mixed pair) | erratum arithmetic |
| D3 relocation coefficient | PASS: (1/3)sum = (9/26)(n^3 - 1), k <= 6; 0.3462 - 9/26 = 3/65000 > 0 | COFUN's 0.3462 is a safe round-up |
| D4 8*65/26244 = 130/6561 | PASS | TENTQ calibration |
| D5 rigorous log intervals | PASS: k* in [160.379708394, 160.379708396], k*_double in [80.939854196, 80.939854198]; FACEB's 81.7 REFUTED | price arithmetic |
| E1 root covariance Q(d lambda) = d(ev lambda), order-averaged S4' map, d = 2, k = 1 | PASS | validates the root-map implementation |
| **E2** D(Q^T B) for a single level-1 link B | **FAIL of GS-BASE's reading**: D(Q^T B) = {(1,1): -1, (4,1): +1} = ev^T d*B exactly; zero off the roots | the top-level "data/residual-type" source is (cc), NOT (CC-0) |
| E3 control: co-closed B | PASS: D(Q^T B) = 0 | E2's root charges are exactly d*B |

What r55t cannot decide (stated in the criteria in advance): no response field Y^p is computed, so
nothing here is evidence about Phi_k(Y^p_{*,0}) or about the actual (TENT-osc); Part E is abelian and
linear; k <= 4, so no level count is measured.

**Erratum to the D5 row above (my own transcription error, corrected at once):** r55t_out.txt prints
the rigorous intervals only to 9 decimals, and both endpoints display identically:
"k* in [160.379708395, 160.379708395]; k*_double in [80.939854197, 80.939854197]" (log10 3 displays
as [0.477121255, 0.477121255]). The endpoints I typed in the table (…394/…396, …196/…198) were not
printed by the script and should be read as the displayed values just quoted. The verdict (PASS;
FACEB's 81.7 refuted) is unchanged: the criteria's test is containment in [160.37, 160.39] and
[80.93, 80.95], which the exact rational endpoints satisfy.

---

## 1. TENTQ.md

**r55t-TQ1 Proposition QN, Sigma_X Q_X(S) = 0 (TENTQ l.127, "### 2.1 Proposition QN"). CONFIRMED.**
Sigma_X chi^5_X = 1 (BFT_B l.2146-2148; r55t B5) gives Sigma_X Q_X = <1, D(S)>; placement ev^{(0->l)T}
preserves totals and <1, d*S_l> = <d1, S_l> = 0 on the torus. Two lines; nothing hidden.

**r55t-TQ2 Proposition QSBP (*): Q_X(S) = Sigma_l <d(ev^{(0->l)} chi^5_X), S_l> (l.147). CONFIRMED.**
Adjointness of the placement and d^T = d*. r55t B2 = B1 exactly on the extremal configuration
(box sum vs collar flux, two code paths), d = 2 (k = 1, 2, 3) and d = 4 (k = 1, 2).

**r55t-TQ3 Q_X != 0, |Q_X| <= 2d Sigma_l pi_l(S_l), attained (l.165-185). CONFIRMED at l = 0
(B1/B2 exact), and analytically at every l:** for a product of one-dimensional unimodal factors with
1-D total variation 2 and sum n/L^l per transverse line, ||d(ev^{(0->l)}chi^5_X)||_1 = 2d(n/L^l)^{d-1}
exactly; times sup_own|S_l| this is 2d·pi_l(S_l). The "currency" reading (the L^{3(k-l)} of the
collar cancels the own->coarse conversion) is right.

**r55t-TQ4 Proposition QFALSE: (NEUT-box) "as stated in BFT_B §36.4 is FALSE, by exactly L^{2k}",
struck (l.189-209; tq1b l.684-700). CONFIRMED as a statement about the source class; one arithmetic
slip; and a scope limit the strike must carry.** Checked as hard as a theorem:
- The object refuted is the one banked. BFT_B l.4193 (§36.4, the DERIVED form, which RS10-5 makes
  binding): "max_X|<chi^5_X D^perp(S)>| <= C·n·||D^perp(S)||_inf", S a general source (§31.3 l.3810:
  "Let S be any source"). TENTQ's witness j_0 = c·sign(d chi^5_{X0}) is a level-0 slot of such a
  source, in the (P0) class. No symbol collision: chi^5 is BFT_B l.2024's quintic tent; D^perp is
  BFT_B l.3963's off-root part.
- The power, exactly (r55t B1-B4, Fractions): Q_{X0} = 8n^3, ||D||_inf = 8 (so the D-ratio is exactly
  n^2), D(c_{X0}) = 8, and **||D^perp||_inf = 6**, so the ratio NEUT-box actually tests is
  R = (8n^3 - 8)/(6n) = (4/3)(n^2 - 1/n): 104/9 at n = 3, 2912/27 at n = 9. So the failure is by a
  clean n^2 = L^{2k} (with constant 4/3), and it cannot be repaired by a constant: the collar bound
  of TQ3 is attained. The d = 2 control behaves as it must (R -> 2, bounded; NEUT-box's n^{d-2}).
- Slip: l.201 writes "(8cn^3 - 8c)/(8c·n) = n^2 - 1"; the quotient is n^2 - 1/n. The stated lower
  bound ">= n^2 - 1" is still true (weaker), so nothing downstream moves.
- **Scope the strike must carry.** BFT_B l.4193-4195 presents (NEUT-box) as a condition that "has to be
  supplied by the source". QFALSE shows the class norms cannot supply it; it does NOT show that the
  contraction's actual rows violate it. "Struck as an open item" is still justified, by TENTQ's other
  two legs: Proposition PINC (TQ5) makes the pinned charge cancel in every pairing (not necessary),
  and GT-ell's first term n^4||D^perp||_inf already exceeds the (P0) currency by n (not sufficient).
  **What QFALSE does NOT support:** the reading "a dipole-neutrality route is risky". It refutes one
  inequality in one currency (box charge vs n·sup D); it says nothing about routes that do not
  measure root/box charges against ||D||_inf. In fact §6 (X1) below shows root charges of
  composite-co-closed sources are harmless for the curvature half by a different mechanism.

**r55t-TQ5 Proposition PINC (l.211-246). CONFIRMED** (algebra: B + P regrouped with
Sigma_w chi^5_X(w)phi(w) = Q_X(phi); given Lemma Gamma-T-op (a), BFT_B §25.1, not re-derived).

**r55t-TQ6 Theorem TQ-INT and "the box charges are eliminated" (l.261-274). CONFIRMED as an identity**
(multiply (*) by Phi(c_X), sum, linearity). "Eliminated" is a reformulation, not a gain; and the
identification of COF-res's root charges D(S^E_0(S))(c_X) with TENTQ's box charges Q_X(S) is
imported from BFT_B §36.5(ii)/Lemma DF(iii), not re-derived here (agree with Codex FACEB R6 on this).

**r55t-TQ7 Lemma TENT-TV (l.276-287). l1 bound CONFIRMED; the pointwise clause |delta_mu(z)| <= 15/(8n)
(l.281) REFUTED for l >= 1.** A level-l link spans L^l fine steps, so the correct factor is
15·L^l/(8n) (capped at 1); at l = k the level-k link joins adjacent roots and the difference is the
full root difference (chi^5_X(c_Y) = delta_XY). Agree with Codex FACEB R11.1. Not used in any bound.

**r55t-TQ8 Proposition TQ-NOGAIN "osc = max_B|Phi_k(v)| exactly" when Phi_k vanishes at a root of B
(l.299-306). REFUTED as stated; conclusion survives.** With osc = max - min, values {-a, 0, a} give
osc = 2a. Correct: max|Phi| <= osc <= 2·max|Phi|. The conclusion (neutrality buys a constant, not a
power) holds. Agree with Codex FACEB R11.2. For the witness (one nonzero corner) equality holds.

**r55t-TQ9 Proposition TGAUGE (l.321-345). CONFIRMED** (telescoping: Q_str d = d A, h_i(d nu) =
A_i nu - ev nu; r55t A7 checks both one-step identities exactly for both h operators, and A3 checks
the composed identity on mu = delta_c at k = 1, 2, 3). The "price" half is ARGUED as labelled (and
later closed elsewhere by TGAUGE_PRICE, outside this batch).

**r55t-TQ10 Theorem TQ (iii)/(iv): deficit "exactly one power of n", calibration 130/6561 = 0.019814
(l.360-390). Arithmetic CONFIRMED (r55t D4; A1 rebuilds 65/26244).** The calibration is the
ORDER-AVERAGED operator's (see X-T6); the reduction (TENT-Q) <= (TENT-osc) is CONFIRMED as an
implication. Whether (TENT-Q) matters at all is decided in §6 (X1): it does not.

**r55t-TQ11 §4.3 "the factor k is upstream; through Sigma_l pi_l the sharp loss is k" (l.551-580).
Spot-checked, CONFIRMED in substance**, and Codex COFUN F11.2 sharpens it: at fixed alpha > 0 the
||.||_Pc route cannot use theta* ~ 1/((k-1)ln L) (theta must exceed alpha), so through ||.||_Pc the
loss is >= L^{alpha(k-1)}; the Sigma_l pi_l bookkeeping (loss k) is the better one.

*Citation correction to r55t-TQ4 (mine):* "Let S be any source" is BFT_B **l.3808** (not l.3810, which is
the (R1) line); "has to be supplied by the source" is BFT_B **l.4194**; D^perp is defined in BFT_B §34.1
("The two parts of the composite divergence", l.3963). Content unchanged.

(One more digit: the D^perp definition line is BFT_B **l.3962**, verified by grep; "l.3963" above is wrong.)

## 2. YSUP.md

**r55t-YS1 Proposition YS-K (l.124-160): support and norms of K_i. Spot-checked at i = 0, CONFIRMED there**
(r55t A4: the order-averaged h_0 kernel lives on block-interior links; max|c| = 10/81, which is YSUP's
"(exact value (10/81)·n_i^{-3})" at i = 0 (l.133); sum|c| = 8/3). i >= 1 not recomputed. Note the
10/81 is the ORDER-AVERAGED operator's value; COFUN's 1/3 for "the same" kernel is a different
operator (X-T6).

**r55t-YS2 "Phi_k(v)/sup_own|v| is dimensionless and carries no k" (l.163), verified by ys1 A5. REFUTED.**
r55t A3: Phi_k(d delta_c)(c) = 3^{-4k} - 1 = -80/81, -6560/6561, -531440/531441 — the very identity
cited as verification is k-dependent. Correct statement: the normalisation introduces no k-dependent
unit factor, and on the (1+|z|)^{-3} profile class Phi_k is bounded uniformly in k; it is not
k-independent (it is for the terminating witness u only). Agree with Codex FACEB R4. Consequence:
FACEB §2.2's "a k-free dimensionless number must be <= L^{-2k}" (FACEB l.142) inherits the error.

**r55t-YS3 Theorem YS-AVG, Theta(n_i^{-2}) per level vs Theta(n_i^{-3}) for a full block average
(l.171-215). Power CONFIRMED analytically; constants NOT-VERIFIED.** The count (per-link weight
n_i^{-(d-1)}, kernel l1 mass ~ n_i, marginal |z|^{-3} l1 mass ~ n_i at d = 4) is right. But the proof
of (i) bounds ||v||_{l1(block)} by T(S) built from the ℓ^∞ SITE-shell count N(s) (l.196-200), while v
lives on LINKS (d per site): the constants 64/96/15.13 look low by up to a factor d = 4. The power,
and hence YS-PHI's ratio L^{-2}, is unaffected. Numerical exponents (ys1b) not re-run.

**r55t-YS4 Theorem YS-CORE (ii): the exact witness u = (1/8)d*delta_p, Phi_k(u) = -65/26244 for every
k >= 2, series terminates (l.229-233). CONFIRMED for the order-averaged h** (r55t A1, A2: k = 2, 3, 4;
Codex FACEB R2 supplies the all-k argument). **But the phrase "the very field BFT_A §38.7 takes as g_0"
(l.230) is REFUTED** (agree GESIGN §2.2): BFT_A l.1712 defines g_0 := d*(chi omega^p), a cut-off
Green's-function dipole (y^p = d*omega^p at r = infinity), not the four-link field u.

**r55t-YS5 Theorem YS-DEC (a): "(TENT-osc) is FALSE, by exactly n^2 = L^{2k}" (l.260-262).
CONFIRMED only in the class form (FACEB's FB-CLASS); NOT-VERIFIED for the actual response.** The
lower bound is exact for u, which is not g_0 (YS4) and not Y^p_{*,0}; the reading at l.252-254 that
substitutes the response for the witness is unsupported (FACEB FB-F3, Codex FACEB R2). And by §6 (X1)
the quantity is not an obstruction to the curvature half in any case.

**r55t-YS6 YS-DEC (b): "the averaging does not beat the core"; the i = 0 level is binding
(l.270-284). CONFIRMED as a structural statement** about Phi_k: the i-th term reads v only on the
level-(i+1) block (r55t A4 support; YS-K), and the i = 0 block has side L = 3 with no averaging. On the
witness the i = 0 share is 243/260 (order-averaged h; r55t A1, D2) or 100% (fixed-order h, where
phi_2 = 0; r55t A5). For the actual response it is ARGUED (needs a Theta(1) core of the named
representative). Moot for the curvature half by X1.

**r55t-YS7 YS-DEC (c) "(TENT-Q) is k-uniform away from p's coarse cell with R_c^{-3}" — ARGUED as
labelled; spot-check: the one-coarse-step oscillation of an R^{-2} profile is plausible; not verified.**

**r55t-YS8 YS-DEC (d) "(Y-sup^loc) FALSE by exactly n" (l.300-307). Spot-check: agree in substance**
(own sup of the response near p is Theta(1) if Y^p_0 = y^p + O(n^{-2}) near p, as Case A/B's
decomposition indicates); this is REVIEW_BFT_B_S9_S10 RS10-7's point. Conditional on that profile.

**r55t-YS9 Proposition YS-PHI ((Phi-conv) PROVEN for the profile class) (l.309-322). CONFIRMED for the
geometric ratio L^{-2}** (from sup|K_i| <= n_i^{-3} and the marginal l1 count); constants subject to the
link/site factor of YS3.

**r55t-YS10 YSUP l.249 normalisation erratum. CONFIRMED.** l.249 lists phi_1 = -1/54, phi_2 =
-17/13122 (un-normalised) beside psi_u = -65/26244 (normalised) "for the unnormalised u"; the
un-normalised total is -130/6561 (REVIEW_BFT_A_S8 l.249-253 has it right). Mixed ratio
phi_1/psi_u = 486/65 = 7.48 (r55t D2), consistent ratio 243/260. Agree with Codex FACEB R3 and FACEB §7.3.

**r55t-YS11 Proposition YS-GT ((GT-sup) "rescued by its threshold", l.326-345) and §2.7's assessment
of the Hölder fallback. ARGUED as labelled; not checked.** Note for the closing paragraph: this is
the face that remains live (§7).

## 3. FACEB.md

**r55t-FB1 Face (b) = (TENT-osc), n = L^k, the square an explicit prefactor on neither leg (FACEB §2.1-2.2,
l.110-150). CONFIRMED by reading** BFT_B l.3976/l.4114-4116 (COF-res: n^2·Sigma_X D(S)(c_X)·
Phi_k(Y^p_{*,0})(c_X)) and l.4130 (f_0 = n^2 d Delta_0^{-1} J_0, side Tn). n is L^k, not n_i, not T.
**The accompanying sentence "Phi_k is dimensionless and carries no k at all" (l.142) is REFUTED**
(r55t-YS2/A3).

**r55t-FB2 Proposition FB-CLASS, witness u = (1/8)d*delta_p, sup_{v in Y} n^2 osc(Phi_k v) >=
2.4768e-3·n^2 (l.273-284). CONFIRMED with the exact constant 65/26244, for the ORDER-AVERAGED h;
the decimal REFUTED as a certificate.** (i) u is co-closed (d*d* = 0), its four links have modulus 1/8
= (1+1)^{-3} at link-base distance <= 1 (C_0 = 1), and Phi_k(u)(c_X) = -65/26244 for k = 2, 3, 4
(r55t A1, A2); the other roots of a cell read only their own level-k blocks, which miss supp u, so
osc = 65/26244 on any cell containing c_X and a neighbour. (ii) 0.0024768 - 65/26244 = 89/2050312500 > 0
(r55t D1): as a LOWER bound the printed decimal is not established by the witness; use the fraction or
0.0024767. Agree with Codex FACEB R2. (iii) **Collision (X-T6):** with the single-fixed-order h that
BFT_B §27.1 describes, the same witness gives Phi_k = -1/72 (r55t A5). The class statement survives
under either operator (both nonzero and k-independent), but the exact constant belongs to the
order-averaged operator, which is the lane's (LINEAR_PACKAGE §1.2). (iv) The class Y is the g_0-clause
class, not the actual-response class (NOT-VERIFIED identification; Codex FACEB R2 agrees).

**r55t-FB3 Corollary FB-NOEST, "no slack: |T_p| = n^2|Phi_k(c_{X_p})||Q_{X_p}|(1+O(n^{-2}))", "at most 2d = 8"
(l.251-255). REFUTED as written.** A universal approximate equality is false: charges at non-core
corners, e.g. a neutral pair with Q_{X_p} = 0, give a nonzero residue while the "leading product"
vanishes; co-exact source slots give zero pairing with positive norm. What survives is worst-case
attainment of the TENT-TV l1 bound (single-corner Phi; r55t B1 at l = 0). The TG-TV lower bound it
also uses is in TGAUGE_PRICE (outside this batch; NOT-VERIFIED). Agree with Codex FACEB R6.

**r55t-FB4 Proposition FB-LOCAL and 243/260 (l.433-455). 243/260 CONFIRMED for the order-averaged h**
(r55t A1 + D2: (1/432)/(65/26244) = 243/260 = 93.46%). **Operator-dependent:** with the fixed-order h
the i = 0 share is 100% (phi_2 = 0; r55t A5). **"Any fix must change h_0" (l.454) REFUTED as a general
implication** (agree Codex FACEB R3): it is a statement about one witness; a response-specific
cancellation or structure need not touch h_0; and by §6 (X1) no "fix" of this term is needed.

**r55t-FB5 Proposition FB-BOOT, "no lower bound on |Phi_k(Y^p_{*,0})| follows at all"; the missing input
is "a sign statement on G_e" (l.304-315). REFUTED.** For the sup over p — which is what refuting a
for-all-p inequality needs — M <= A + B + eps·M and M >= |Phi_k(Y^p)| >= A - B - eps·M give
**(A - B)/(1 + eps) <= M <= (A + B)/(1 - eps)**, i.e. M >= (2/3)max(A - B, 0) at eps = 1/2, with no
sign hypothesis (r55t C2, 200 exact instances; C3 shows 2/3 is sharp). FACEB's error is substituting
its upper bound for M into a pointwise reverse triangle inequality. A pointwise bound can indeed fail
(r55t C1: y = (0, 2) from a = (1, 1)), and a sign condition G >= 0 is neither necessary nor sufficient
(Codex's G >= 0 examples). Agree with Codex FACEB R1. Also moot at r = infinity (GS-ZERO, §4).

**r55t-FB6 "dimensionless => k-independent" (l.142, l.669). REFUTED** (r55t A3; = YS2). Agree Codex R4.

**r55t-FB7 Proposition FB-ONE-LEG (l.216-222), ARGUED. The trivial half CONFIRMED** (both terms are
linear in D(S) and vanish at D = 0). **The consequential half — removing face (b) leaves (NC-Gamma)
failing by L^{2k-3} from the sigma-spike term — NOT-VERIFIED**: it rests on BFT_A §38.6's ARGUED
sizing (sigma ~ 0.003 measured) and, as GESIGN §7 itself notes, Lemma RC and COF-res are stated for
different source classes. See r55t-GS8 for the PROVEN upgrade (refuted) and §6 for why the D^root leg
is not an obstruction at all.

**r55t-FB8 The price (§6, l.461-560). Baseline rows CONFIRMED** (P(k) = (2k-3)log10 3; k* = 160.380
against DX' with C_Omega = 1 and C_SR omitted; r55t D5 by rigorous rational intervals). **"k* ~ 81.7"
in the doubled currency (l.537) REFUTED: k*_double = (k* + 3/2)/2 = 80.940** (r55t D5; agree Codex R5).
X1 (self-map reading) and X2 (eta <-> DX'/epsilon_1 identification) remain unestablished, as FACEB
itself says; every decade figure there is a courtesy figure. Note: by §6 (X1) the n^2 being priced is
not a term f_0 must carry, so the whole price is of a bookkeeping artefact.

**r55t-FB9 Proposition FB-BIANCHI (l.365-371). REFUTED in its type claim** "D(S) is entirely inside the
divergence-form part" (l.367): D(S) is a 0-form (Sigma ev^T d*S_l), the "co-exact part" is a statement
about 1-form slots S_l = delta W. Agree with Codex FACEB R8. The usable fact (T_p depends on S only
through D(S)) is TQ-INT.

**r55t-FB10 Pre-registered verdict "SHARP-AND-FATAL ... not binding" (l.685-689). REFUTED as a
conclusion about f_0** — sharp for the class witness (FB2), unestablished for the response (FB-F3), and
not fatal because the residue is not a separately-bounded term of f_0 (§6, X1). Agree with Codex R9
that the broad no-go retreats from its own quantifier.

**r55t-FB11 Gate fb1 (A1-A7). NOT re-run by me.** Codex FACEB R7's mutation (incidence ×2 passes A1-A6)
is plausible from the description (A4's acceptance tests booleans, not values); I did not verify it.

## 4. GESIGN.md

**r55t-GS1 What G_e is (§2.1-2.2, l.133-170). CONFIRMED by reading** BFT_A l.1705-1718 (Lemma PC, Lemma LD)
and l.1874-1917 (§23.1-23.3): G_e = P e, e = d*G' - (Q_str^{(0->k)})^T J, G' = chi h_p - [Delta_0, chi]omega^p.

**r55t-GS2 Proposition GS-ZERO: at chi == 1 (r = infinity), G_e == 0 identically (l.192-205). CONFIRMED,
and NOT vacuous — both conditions the brief named hold:**
- *Lemma LD admits r = infinity at every k, T:* BFT_A l.1711, verbatim "Let chi := Phi_{r,p} with
  1 <= r <= M/4, **or chi :== 1 ("r = infinity")**" — no restriction on k or T in the statement; the
  proof §23.3 step 1 treats it ("For r = infinity, chi == 1 ..."), and BFT_A uses it in Case B (l.2009,
  l.2451, l.3570-3573 "No bootstrap").
- *Y^p does not depend on r:* BFT_A l.1691-1692 defines Y^q as a minimiser of E_src with B_k = 0 and the
  single source G_0 = delta_q — no cutoff in sight; r enters only the split Y^p = g + Z.
- *The computation:* at chi == 1, G' = h_p (constant), (d*G')_nu = Sigma_mu[G'(z - e_mu) - G'(z)] = 0, so
  J = F d*G' = 0, e = 0, G_e = P0 = 0 and s_i = 0: Y^p == g + Z with Z the source-free data response.
**Caveat GESIGN itself flags (its hostile item 1), CONFIRMED by reading:** at r = infinity Lemma EX's shell
count is J + 2 with L^J <= M/4 = Tn/4 (BFT_A l.1928-1930), i.e. ~ k + log_L T, and Case B's constants
(e^{128 m' L^c}) are stated only for T < 8L^c; so GS-ZERO removes the bootstrap but moves the
T-uniformity question into B = sup|Phi_k(Z''_0)| (GESIGN's (GS-B)). The textual nit (BFT_A l.1713/l.1904
"G' = 0 for r = infinity" vs G' = h_p) is real but minor: l.1713's own carve-out "apart from the term
chi h_p" covers it.

**r55t-GS3 "The 1/2 is a threshold, not a size" (§3.2, l.249-260). CONFIRMED** (BFT_A l.2344-2346:
Sigma|G_e| <= 1738 C_j L^{-c}; "<= 1/2 holds for L^c >= max(260, 3476 C_j)"). §4.2's table arithmetic
(3476, 6952, 347600; T >= 27808, 55616, 2.7808e6 times C_j; log_3 100 = 4.19) CONFIRMED (spot).

**r55t-GS4 Lemmas GS-ZS, GS-FM, GS-MOM (l.262-292). CONFIRMED analytically** (pair d*e = 0 with z_nu,
resp. z_mu; Delta z_mu = 0). Minor: GS-MOM's "every r, finite or infinite" uses compact support in a lift;
at r = infinity e = 0 anyway, so nothing depends on it. gs1 not re-run.

**r55t-GS5 Proposition GS-WINDOW (l.316-330). Algebra CONFIRMED as a POINTWISE bound** (r55t C1 realises
its degenerate point). **Its adjudication "that, and only that, is FB-BOOT's 'no lower bound at all'"
is REFUTED in part:** for the sup over p, M >= (A - B)/(1 + eps) > 0 whenever B < A, for every eps < 1
including 1/2 (r55t C2). FB-BOOT is wrong even at eps = 1/2; GESIGN repeats its pointwise framing.

**r55t-GS6 Corollary GS-SHARP (l.375-389). CONDITIONAL as labelled** on (GS-A) (A = |Phi_k(g^natural_0)|
k-free and positive, with g_0 = y^p, not u) and (GS-B) (Phi_k bounded on the inv-ball). Add the T-caveat
of GS2. Moot for the curvature half by §6 (X1).

**r55t-GS7 Proposition GS-BASE: "K'_0 = 0 by definition (BFT_A l.2761) ... Xi^T N_B = 0 identically ...
the whole first source is composite-co-closed: (CC-0) holds exactly" (l.461-476).**
- *K'_0 = 0 at l.2761:* **CONFIRMED** (BFT_A l.2761: "K_0 = -Xi in this sign convention; K'_x := K_x - K_0").
- *(CC-0) at the first step:* **REFUTED.** Both identities it uses hold only as functionals on gauge
  functions trivial at the level-k roots: BFT_A §33.3 proves Lemma CD "on such xi" (xi vanishing at the
  level-k roots), and [RBA7-fix] P7-3 (BFT_A l.3393-3394) states "(GI) is assumed only for gauges trivial
  at level k, which is Lambda_*"; "Xi^T N B = 0" rests on r_{k-1}(Xi xi) = 0, which holds only when
  ev^{(k)}xi is constant (x_k = B_k is data and is not transformed). They give **(cc)** (D vanishes off
  the level-k roots), not (CC-0). The root values are not zero in general: with N B = kappa_{k-1}
  Q_{k-1}^T B_k (from (kappa/2)||Q x_{k-1} - B_k||^2), transposed root covariance (BL-2 (c),
  d*Q^T = ev^T d*) gives **D(N B) = kappa_{k-1} ev^{(0->k)T} d*B_k**, nonzero at every root where the datum
  is not co-closed. r55t E2 computes the k = 1 instance exactly with the order-averaged S4' map:
  D(Q^T B) = {(1,1): -1, (4,1): +1} = ev^T d*B for a single coarse link B, zero off the roots; control
  E3 (co-closed B) gives 0. Nonabelian, the root values of D(N^0(0;B)) are not controlled by Lemma CD
  at all.
- *The conclusion "the first step meets no off-critical obstruction"* survives for a DIFFERENT reason:
  the first source is (cc), and by §6 (X1) root charges of (cc) sources are harmless for the curvature
  half (conditional on two banked theorems). So: derivation REFUTED, conclusion CONDITIONALLY true.
- GS-BASE also cites Corollary COF-crit for "k-, T- and Gamma-uniformly"; REVIEW_BFT_B_S9_S10 S10-6
  refutes COF-crit's application to rows (factor k). Whether the x = 0 source escapes that factor is
  NOT-VERIFIED.

**r55t-GS8 Proposition GS-NOCIRC, "Clause (FB-CIRC) is not circular ... the base step is free" (l.514-520),
i.e. the brief's "the circularity does not close". NOT-VERIFIED.** (i) Its anchor (GS-BASE) is argued
wrongly (GS7), though repairable via X1 for the root part. (ii) From step 1 on, the iterates are not
critical, the sources carry off-root divergence D^perp != 0, and that part — face (a), not (b) — is what
GS-TRANSIENT's O(k)-step transient is about; GESIGN itself records CIRCLE-PARTIAL with the transient's
self-map property open. (iii) A contraction argument needs estimates for the DIFFERENCE sources
N^0(x_j) - N^0(x_{j-1}) along the orbit, not only at the iterates; (gamma)'s "ball vs orbit" critique
does not remove that. So "not circular" is a reframing; the content (D^perp control at non-critical
iterates) is open.

**r55t-GS9 Lemma GS-STEP (l.482-492). CONFIRMED** (substitute the definition of x_{j+1} into
grad F = Hx - N B - N^0).

**r55t-GS10 Proposition GS-ONELEG, FB-ONE-LEG "upgraded from ARGUED to PROVEN" (l.607-620). REFUTED as an
upgrade.** Lemma RC (BFT_A l.3545-3547) is an identity for f^sharp_0 - f^E_0 (two gauge-fixed responses)
for a general source; COF-res (BFT_B l.4112-4120) is an identity for f_0 minus Theorem COF's covered
part, for a Setting LIN^cc source. Different compared quantities and different source classes — GESIGN
itself flags the class mismatch at l.625-630 and then still labels the merger PROVEN. What is true and
trivial: sigma in Lambda_* vanishes at the level-k roots, so RC's pairing sees D^perp while COF-res sees
D^root (complementary supports); both are linear in D and vanish at D = 0. "One pairing n^2<D, Psi^p>
split by root level" is not established. And by §6 (X1) the D^root half is not an obstruction, so the
two "defects" do not have the same status.

**r55t-GS11 (R1)-(R4) of §6.5. (R1) CONFIRMED as a reduction (one line). (R2) ARGUED as labelled. (R3)
reported FAILED — agree. (R4) "sufficiency PROVEN-HERE" NOT-VERIFIED** (a sketch: the dipole-level
neutrality against a (1+R)^{-2} profile is asserted, not derived with constants).

**r55t-GS12 The g_0 / u correction (§2.2, l.155-169). CONFIRMED** (BFT_A l.1712: g_0 := d*(chi omega^p);
at r = infinity g_0 = Delta_0^{-1}d*delta_p = 8 Delta_0^{-1}u since d*h_p = 0).

*Line corrections to §4 (verified by grep after writing):* GESIGN §3.2 begins at l.231 (not 249; l.249 is
Lemma GS-ZS); the Lemmas GS-ZS/FM/MOM run l.249-290; Corollary GS-SHARP is at l.370; BFT_A's P7-3 "(GI) is
assumed only for gauges trivial at level k" is at l.3394. Content unchanged.

## 5. COFUN.md

**r55t-CF1 "The target was stale" (I-F1, l.155-165). CONFIRMED.** BFT_B l.3802 is §31.2, inside "Session 9"
(BFT_B l.3571-3945); §35.5 Theorem COF (l.4074-4104) and §35.7 COF-res with [S10-fix 1] (l.4112-4126)
are "Session 10" (from l.3946). The brief's "single smallest remaining missing input" cites superseded
text. Agree with Codex COFUN F7 that the staleness is real — and, with F7, that "already decided FALSE"
is not established (CF2).

**r55t-CF2 Three classes share the name (CO-fun); one is FALSE as stated and it is D1's class (§2.0-2.1,
l.93-160).**
- *Three classes (lw) ⊊ (CC-0) ⊊ (cc):* **CONFIRMED** (definitions; Codex F7 gives strictness examples).
- *D1's class is (cc):* **CONFIRMED by reading** (BFT_B l.3575: D1 restates (NC-Gamma) "for
  composite-co-closed sources plus a remainder bound"; BFT-5 clause (b), l.3831: "every
  composite-co-closed source").
- *"(CO-fun)[cc] is FALSE as stated" (l.155; S10-11; COF-res): **REFUTED, conditionally on two banked
  theorems** (§6, X1): the sup half of (CO-fun)[cc] follows from Theorem COF plus LINEAR_PACKAGE's
  data-to-curvature kernel bound. Independently of X1 the falsity was never established: S10-11/COF-res
  argue from one unbounded term of a decomposition whose complement is not shown bounded for D != 0
  (exactly RS10-6), and COFUN's own §6.2(iv) concedes no unbounded f_0 is exhibited while §2.1, §7, §9
  keep "FALSE"/"refuted"/"not an open item". Agree with Codex COFUN F2/F7 and go further.

**r55t-CF3 The exponent window (§2.2, l.170-205). COFUN's conclusion CONFIRMED against the SOURCE; its
quotation is wrong; Codex F11.1 is right only against the misquote.** COFUN l.192 quotes BFT_A as
"alpha <= theta <= 1 - alpha <= 3/4". The source says, at l.396: "Window alpha <= theta <= 1 - alpha (so
alpha <= 1/2)", and at l.827 (binding [RBA2-fix] B4): "0 < alpha <= theta <= 1 - alpha (so alpha <= 1/2),
**e.g.** alpha = 1/4, theta in [1/4, 3/4]". The "<= 3/4" belongs to the example. Against the source the
intersection with alpha < theta_c is alpha in (0, 1/2), theta_c in (alpha, 1 - alpha] — COFUN's stated
window. **I disagree with Codex F11.1** (its alpha in [1/4, 1/2) follows only from COFUN's misprint) and
**agree with F11.2** (theta* = 1/((k-1)ln L) is inadmissible at fixed alpha once (k-1)alpha ln L >= 1;
the ~25(k-1) optimisation is unavailable, and through ||.||_Pc the loss is >= L^{alpha(k-1)}).

**r55t-CF4 Handle 1: "sharp" norms ||h_l^T||_{inf->inf} = (L-1)/(2L) = 1/3, ||h_l^T||_{1->1} = 8/3, "3x
sharper", "dimension-blind" (§3, l.207-262). 8/3 CONFIRMED; 1/3 REFUTED as the sharp constant of the
lane's h_l (X-T6).** COFUN rebuilds h_l with ONE fixed coordinate order, following BFT_B §27.1 l.3589 /
§29.2 l.3696. The lane's h_l is defined by Q_l = Q_str,l - d∘h_l with Q_l the linearised S4' root map
(BFT_A l.446-447), and LINEAR_PACKAGE §1.2 (l.64-73) defines it as "h(A)(X) := avg_sigma avg_{y in B(X)}
integral over P^sigma(c_X -> y)" — averaged over the 4! orders (also BFT_A l.895, l.1112, l.3530 "24-order
average"). r55t A4: order-averaged max|c| = **10/81**, fixed order 1/3; both l1 = 8/3. In general the
order-averaged root-link coefficient is (L^d - 1)/(2 d L^d) (binomial sum; = 10/81 at d = 4, L = 3), so
the lane's operator is NOT dimension-blind, and it is 8.1x below FT (i)'s 1 in l^inf, not 3x. Every
bound that used 1/3 remains valid (10/81 < 1/3); "sharp" and "dimension-blind" are wrong for the lane's
operator. Codex COFUN F9 CONFIRMED 1/3 "at the stated centre-root convention" — I agree for the
fixed-order operator and DISAGREE that this confirms the lane's handle (it does not test the definition).

**r55t-CF5 Handle 2: no hidden L^{k-l} (§4, l.264-330). CONFIRMED** (unit-conversion exponent
-3(l - l'), k-free; prefactor 2d·max|c| = 8/3 with the fixed-order constant, **80/81** with the lane's).

**r55t-CF6 Lemma CO-pin (§6.1, l.380-400), PROVEN-HERE. CONFIRMED** (agree Codex F1). For S in (cc),
<C(j), d lambda> = <d*C(j), lambda> = 0 for lambda constant on the roots; Hölder; n^2·n^{-3}·n = 1. It is
essentially the definition of (cc). One input needs narrowing: d*C(j) = D(S) (Lemma DF-cc (i)) holds
only if the residual slots carry no divergence, which fails for a non-co-closed top residual slot
(X-T7); CO-pin survives with D(S^j), which is also (cc).

**r55t-CF7 The relocation to "coarse size 0.3462·n^3·max|Q_X|" (§6.2(ii)-(iii), l.425-445).**
- *The inequality:* **CONFIRMED as an upper bound** (r55t D3: coefficient (9/26)(n^3 - 1) exactly with
  the fixed-order constant; 0.3462 is a safe round-up). With the lane's order-averaged constant it is
  (10/81)(27/26)(n^3 - 1) = (5/39)(n^3 - 1) ~ 0.128 n^3. Same power.
- *"(CO-fun)[cc] <= (YH-pin) and (ROOT-sup)":* CONDITIONAL/ARGUED (Codex F6 reconstructs it with the
  residual bookkeeping; not re-derived here).
- *(ROOT-sup) false on the class:* **CONFIRMED** (Codex F4's L-edge path between adjacent roots:
  n^3 max|Q_X| / ||j||_Pc = L^{3k-3-theta_c}); **the printed ">=" at l.441 is REFUTED, must be "<="**
  (pi_{k-1} <= L^{-theta_c}||j||_Pc by definition of the max; equality for a top-only source). Agree F4.
- *"A second, independent route to the same blow-up":* **REFUTED** (agree Codex F2):
  <B(D), Y> = Sigma_i <R_{i+1}D, h_i Q_str^{(0->i)}Y> = <D, Phi_k Y> — the same object, estimated in
  sup instead of paired. And neither route shows f_0 grows (X1: it does not).

**r55t-CF8 "It discharges one half of RS10-6" / the gauge-side obstruction has disappeared (§6.2(i), (v),
l.404-426, l.462-468). REFUTED** — I agree with the tail of Codex COFUN (F3, F5): RS10-6 (REVIEW_BFT_B_S9_S10
l.897-899) asks about d* of A = Sigma_l (Q_str^{(0->l)})^T j-hat_l and step (c)'s representative freedom
for A; CO-pin licenses Lambda_0-freedom for C = A - B(D), a different object (Codex F5's k = 1 example:
<A, d lambda> = 1/81 for lambda in Lambda_0; the computation is operator-independent since
h_0(d lambda) = mean - root value for both h). CO-pin trades RS10-6 for a NEW open input (YH-pin), whose
constraint set is T^4 - 1 root equalities per Lie-algebra component (624 at T = 5), not "one linear
constraint" (l.418). It does not show the gauge side is unobstructed.

**r55t-CF9 The universal negative "no per-level sharpening can ever remove the k-factor" (§4.3(gamma),
§7, l.320-330, l.480-490). REFUTED as stated; a narrow form CONFIRMED.** (i) Its premise "the funnel only
adds to each pi_l(j-hat_l)" is false (Codex F10's (cc) example: pi_1 54 -> 45 with the fixed-order h; with
the lane's order-averaged h the root-link correction is -10/81 and sup|j-hat_1| = 152/81 < 2, still a
decrease). (ii) A per-level estimate WITH level decay removes k: BFT_A Proposition SR (l.2808-2811)
does exactly that under (PW-l1) ("the level-l term is <= C(k-l+1)L^{-(k-l)/2}eta^2 ... so the level sum is
geometric"). Narrow true form: constant-factor sharpening of the two handles cannot remove the level
count of the triangle-inequality sum, which is already present in Sigma_l pi_l(j_l) when the funnel
vanishes (level-wise co-closed rows). Agree with Codex F10.

**r55t-CF10 §5(a): "Lemma CD's output is (CC-0) or nothing — it never lands in the gap" (l.349-356).
REFUTED in its reasoning.** Lemma CD is an identity on Lambda_* (GS7), so at a critical point it gives
(cc). The root values are fixed by an exact telescoping: with (Hx)_0 = d*dx_0 + kappa_0 Q_0^T r_0,
(Hx)_l = -kappa_{l-1} r_{l-1} + kappa_l Q_l^T r_l, N B = kappa_{k-1} Q_{k-1}^T B_k, d*d* = 0 and
d*Q^T = ev^T d*, one gets **D(Hx - N B) = kappa_{k-1} ev^{(0->k)T} d* r_{k-1}(x; B)** for every x
(r_{k-1}(x;B) = Q x_{k-1} - B_k). At a critical point N^0 = Hx - N B, so D(N^0)(c_X) =
kappa_{k-1}(d* r_{k-1}(x;B))(X), which no cited lemma sets to zero for the nonabelian functional. The
same over-reading is in BFT_B §35.6 (l.4108: "as an identity of level-0 functions ... the level-k roots
included") — outside this batch; flagged in §8. By X1 it is harmless.

**r55t-CF11 The erratum against BFT_B l.3810 "D(S^E_0(S)) = 0" (§5(b)). CONFIRMED** as a statement about
the level-0 function (agree Codex F8; the formula is at l.4202). Notational note: BFT_A Lemma GE (c)
(l.2786) writes the same "= 0" for Xi^T as a functional on Lambda_0, where it is correct — a D-vs-Xi^T
collision rather than an error in BFT_A.

**r55t-CF12 cf1 gates and provenance (§8, §10). NOT re-run by me.** Codex F12 (C2's OR-vs-AND; C3 cannot
fire; two runs at M = 2) and F13 (overwritten criteria) are specific and plausible; I did not verify them.

**r55t-CF13 Codex F14 (j-hat_0 has two definitions). CONFIRMED by reading** BFT_B l.3590 ("j-hat_0 :=
j_0") against Lemma DF-cc (ii)'s (dagger) at l.4045, which at k = 1 needs j-hat_0 = j_0 + h_0^T psi_0.

**r55t-CF14 Codex F15 (D(S^s) = 0 not justified at the roots). CONFIRMED and SETTLED by r55t E2** — see X-T7.

*Line corrections to §5 (verified by grep after writing):* COFUN §2.2 is l.167-203, §3 l.204-260, §4
l.261-330 with (gamma) at l.318, §6.1 l.383-401, §6.2 l.402-468, §7 from l.470; BFT_A's "Q_l := the
linearised S4' root map" is l.445. Content unchanged.

(Line fix: BFT_A Lemma GE (c)'s "D(S^E_0(S)) = 0" is at l.2780-2782, not l.2786.)

## 6. Cross-cutting findings (each affects several of the five files)

### X-T6 — Symbol collision: two different operators are both called h_l. CONFIRMED (r55t A4, A5).
- **The lane's operator is ORDER-AVERAGED.** BFT_A l.445-447 defines h_l by Q_l = Q_str,l - d∘h_l with
  Q_l "the linearised S4' root map"; LINEAR_PACKAGE l.70-72: "h(A)(X) := avg_sigma avg_{y in B(X)}
  integral over P^sigma(c_X -> y) A" (sigma over the 4! orders); BFT_A l.895 ("the 24 orders, as in
  S4'"), l.1112, l.3530. TENTQ tq1, YSUP ys1, REVIEW_BFT_A_S8 rev8 and Codex FACEB all compute this one.
- **BFT_B §27.1 (l.3589) and §29.2 Lemma FT (i) (l.3696) describe it with "a fixed coordinate order"**,
  and COFUN §3 / cf1 (and Codex COFUN F9, following COFUN) compute that one.
- **Effects, exact:** h_0 kernel max|c| = 10/81 (lane) vs 1/3 (fixed); l1 row sum 8/3 for both. The
  witness funnel: Phi_k(u) = -65/26244 (lane) vs -1/72 (fixed order 0123); i = 0 share 243/260 vs 1.
  No upper bound written with 1/3 becomes false (10/81 < 1/3); every "sharp", "exact" or
  "dimension-blind" statement made with the fixed-order kernel is about the wrong operator.
- Support statements (paths stay in the block) hold for both, which is why the collision was silent.

### X-T7 — Top-level root charges: (cc) is not (CC-0) at level k - 1 -> k. CONFIRMED (r55t E2, E3).
Transposed root covariance (BL-2 (c): d*Q^T = ev^T d*) gives, for ANY level-(k-1) source of the form
Q_{k-1}^T v (v a level-k 1-form), **D = ev^{(0->k)T} d*v**: root-supported, neutral, and nonzero unless
d*v = 0. r55t E2 is the exact k = 1 instance (order-averaged S4' map, d = 2): D(Q^T B) = ev^T d*B with
charges -1, +1 at the two roots; E3 (co-closed B) gives 0. Three places in or next to this batch read it
the other way:
1. GESIGN GS-BASE (v = kappa B_k, the data source N B): refuted above (r55t-GS7).
2. BFT_B Lemma SPLIT (l.4033-4035; outside this batch, Codex COFUN F15 flagged the gap): "D(S^s) = 0" is
   false for a non-co-closed TOP residual slot (v = s_{k-1}): D(S^s) = ev^{(0->k)T}d*s_{k-1}. Its proof's
   "r_i(x + Xi lambda) = r_i(x) for every lambda" fails at i = k - 1 unless ev^{(k)}lambda is constant
   (x_k = B_k is data and is not transformed). Repair (one line): at B_k = 0, -<s_{k-1}, r_{k-1}(x)> =
   -<Q^T s_{k-1}, x_{k-1}>, so reclassify Q^T s_{k-1} as a plain level-(k-1) current; then SPLIT holds
   and Theorem COF's proof is unaffected. Lemma DF-cc (i) "d*C(j) = D(S)" needs the same reading.
3. BFT_B §35.6 (Corollary COF-crit) reads Lemma CD as "an identity of level-0 functions ... the level-k
   roots included"; BFT_A proves it only on Lambda_* (§33.3 "on such xi"; P7-3 at l.3394). By the exact
   telescoping of r55t-CF10, the root values at a critical point are kappa_{k-1}(d* r_{k-1}(x;B))(X).
   (ARGUED: they vanish in the abelian linear setting by level-k gauge covariance of the data; not
   shown for the nonabelian functional.) Outside this batch: flagged, not adjudicated.
All three are rendered harmless by X1 below; the text should still be corrected.

### X1 — Root charges of composite-co-closed sources are data. (Reviewer's derivation.) PROVEN as an
### implication of two banked theorems; sup half only; NOT independently checked; it reverses the
### "(CO-fun)[cc] is FALSE" verdict that the TENTQ -> YSUP -> FACEB -> GESIGN -> COFUN chain rests on.

*Statement.* Let S be a Setting LIN^cc source (B_k = 0; BFT_B l.3586) in the (P0)+(Pl-c)+(G)+(R)
classes, composite-co-closed: D(S) = Sigma_X q_X delta_{c_X}, Sigma_X q_X = 0. Put
c(S) := Sigma_{l<k} pi_l(j_l) + ||s_{k-1}||_inf (the top residual in level-k units). Then, k- and
T-uniformly,
  **||f_0(S)||_inf <= C_fun·N(S') + (C_D/kappa_{k-1})·c(S),  N(S') <= N(S) + L^theta(1 + 2d L^3 w)·c(S),**
with C_fun Theorem COF's constant, N the class norms of (CO-fun)'s right side, C_D the data-to-f_0
kernel constant of LINEAR_PACKAGE Theorem 4.2 (ii), and w = max|h-kernel| (10/81 at d = 4, L = 3).

*Proof.* (1) **Cut bound.** For a set A of level-k sites, Sigma_{X in A} q_X = Sigma_{z in A~} D(S)(z)
(D vanishes off the roots; A~ = the union of the level-k blocks of A) = Sigma_l Sigma_{Z in A~_l}
(d*S_l)(Z) (placement) = Sigma_l [flux of S_l across the boundary of A~_l] (discrete Gauss). The
G-slots give 0 (d*d* = 0); the residual slots l <= k-2 cancel pairwise (Q^T s_l at level l against
-s_l at level l+1, by d*Q^T = ev^T d*); the top residual gives its level-k flux across the boundary of
A. Each level-k boundary face carries L^{3(k-l)} level-l links. Hence |Sigma_A q| <= |boundary(A)|·c(S).
(2) **Gale-Hoffman** (a neutral demand on an undirected graph with uniform capacity c is feasible iff
every cut satisfies |demand(A)| <= c·|boundary(A)|): there is a level-k 1-form b with d*b = q and
||b||_inf <= c(S). The bound is local, hence T-uniform.
(3) **Subtract a data-type current.** S' := S - (plain level-(k-1) current Q_{k-1}^T b). Then
D(S') = D(S) - ev^{(0->k)T}d*b = 0 (X-T7's identity), so S' is (CC-0), and Theorem COF gives
||f_0(S')|| <= C_fun N(S'); pi_{k-1}(Q^T b) <= L^3(L^{-3} + 2d w)||b||_inf because
Q^T = Q_str^T - h^T d* (BL-2 (c) proof, BFT_A l.609). (If S has a non-co-closed top residual slot,
first apply X-T7's reclassification so that Theorem COF's slot split is valid.)
(4) **The subtracted current IS data.** At B_k = 0 the plain current Q_{k-1}^T b enters E_src exactly
as the datum B_k = b/kappa_{k-1} does: (kappa/2)||Q x_{k-1} - B||^2 = (kappa/2)||Q x_{k-1}||^2 -
<kappa Q^T B, x_{k-1}> + const (BFT_A §7.1 l.445-452). Same minimisers, same f_0. LINEAR_PACKAGE
Theorem 4.2 (ii) (l.211-217: the B_k -> f_0 kernel obeys |K| <= M e^{-m'|X|_1}, uniformly in k >= 1
and T; cited PROVEN at BFT_B l.316-317) gives ||f_0||_inf <= C_D||b||_inf/kappa_{k-1}.
(5) Linearity. ∎

*What it rests on, and what it does not cover.* Theorem COF (CONFIRMED for sources by
REVIEW_BFT_B_S9_S10 S10-6, with X-T7's one-line repair) and LINEAR_PACKAGE Theorem 4.2 (ii) — neither
re-derived here; Gale-Hoffman (classical); BL-2 (c) (r55t E1/E2 check the identity exactly at k = 1).
It covers ||f_0||_inf only: the Hölder half needs a Hölder bound for the data-to-f_0 map, not checked.
No numeric check of X1 was run (k-uniformity cannot be measured at small k). **Because it reverses a
CONFIRMED review verdict (S10-11), it should get an independent hostile check before PROOF.md moves.**

*Consequences.*
(a) The sup half of (CO-fun)[cc] holds; "(CO-fun) as stated is FALSE" (BFT_B §35.7, S10-11; COFUN
§2.1/§7/§9) is refuted, conditionally on the two banked theorems.
(b) COF-res's premise "with every other term bounded as in Theorem COF" (BFT_B l.4114) fails whenever the
residue is large. On the data family S = kappa Q^T B_k (q_X = kappa(d*B_k)(X)) f_0 is bounded by
C_D||B_k||, while the residue n^2 Sigma_X q_X Phi_k(Y^p_*)(c_X) is n^2|q| times the representative's
funnel; if that funnel is Theta(1) at a root next to p, as YSUP and FACEB argue, the complement cancels it.
RS10-6's open point is thereby resolved against COF-res. (This is also why TGAUGE_PRICE found the gauge
shift to be exactly a null operation: the split, not f_0, is representative-dependent.)
(c) So (TENT-Q), (TENT-osc), face (b), the G_e sign question, FB-NBHD's circularity, (YH-pin) and
(ROOT-sup) are not obstructions to the curvature half on (cc). TENTQ's, YSUP's and FACEB's exact
statements about Phi_k and the residue remain true, as statements about a bookkeeping term.
(d) For the contraction's rows c(V) = Sigma_l pi_l(V_l) is about k times the per-level row size: the level
count reappears exactly where S10-6 put it, and (SPD)/(W2) is still needed.
(e) X-T7's root-level questions ((CC-0) vs (cc) at x_0 = 0, at critical points, for the top residual) are
harmless.

(Line fix: the transposed form "Q^T = Q_str^T - h^T d*" is BFT_A l.608, not l.609.)

## 7. Codex verdicts used, and whether I agree

Files as on disk at 22:56Z: CODEX_REVIEW_FACEB.md (41162 B, finished, ends with a stdout summary);
CODEX_REVIEW_COFUN.md (36462 B, mtime 22:20Z — it had grown from 15390 B in the brief's era and from 28586 B
when I first read it at 22:17Z; it now runs F1-F15 plus summary and closing sections and ends cleanly).

| Codex item | its verdict | mine | note |
|---|---|---|---|
| FACEB R1 FB-BOOT | REFUTED; M >= (2/3)max(A-B,0) | AGREE | r55t C1-C3 |
| FACEB R2 witness / decimal | CONFIRMED / decimal wrong way | AGREE | + X-T6: exact constant is the order-averaged operator's |
| FACEB R3 243/260, 486/65, "must change h_0" | CONFIRMED / CONFIRMED / REFUTED | AGREE | + X-T6: 243/260 is operator-dependent |
| FACEB R4 dimensionless => k-free | REFUTED | AGREE | r55t A3 |
| FACEB R5 prices; 81.7 | CONFIRMED; 80.940 | AGREE | r55t D5 |
| FACEB R6 FB-NOEST | REFUTED | AGREE | |
| FACEB R7 fb1 gate power | REFUTED (mutation passes) | NOT CHECKED | plausible; I did not run fb1 |
| FACEB R8 degree conflation | REFUTED | AGREE | |
| FACEB R9 broad no-go | REFUTED | AGREE | X1 makes the no-go moot |
| FACEB R10 citation drift | REFUTED (two anchors) | PARTLY CHECKED | TQ-INT is TENTQ l.261-274 (agree) |
| FACEB R11 TENT-TV factor; osc = max | REFUTED both | AGREE | |
| COFUN F1 CO-pin | CONFIRMED | AGREE | |
| COFUN F2 independent route; falsity | REFUTED; NOT-VERIFIED | AGREE, and stronger | X1 refutes the falsity conditionally |
| COFUN F3 "one constraint"; RS10-6 | REFUTED (T^4 - 1) | AGREE | |
| COFUN F4 ROOT-sup; ">=" | CONFIRMED; REFUTED | AGREE | |
| COFUN F5 RS10-6 discharge | REFUTED | AGREE | the brief's "tail" claim: agreed |
| COFUN F6 TENT-Q <=> ROOT-sup | REFUTED | AGREE | |
| COFUN F7 staleness; three classes | CONFIRMED; falsity NOT-VERIFIED | AGREE, and stronger | X1 |
| COFUN F8 l.3810 erratum | CONFIRMED | AGREE | + D-vs-Xi^T notational note |
| COFUN F9 handle norms 1/3, 8/3 | CONFIRMED | **PARTLY DISAGREE** | right for the fixed-order operator COFUN built; not the lane's h (10/81; X-T6) |
| COFUN F10 universal negative | REFUTED premise; NOT-VERIFIED | AGREE | + BFT_A Prop. SR is a per-level sharpening that removes k |
| COFUN F11.1 window [1/4, 1/2) | REFUTED | **DISAGREE** | follows only from COFUN's misquote; the source window gives (0, 1/2) |
| COFUN F11.2 theta* infeasible | REFUTED | AGREE | |
| COFUN F12, F13 cf1 gates/provenance | REFUTED / NOT-VERIFIED | NOT CHECKED | |
| COFUN F14 j-hat_0 collision | REFUTED | AGREE | read l.3590 vs l.4045 |
| COFUN F15 D(S^s) = 0 at roots | NOT-VERIFIED | AGREE, and SETTLED | r55t E2 is the counterexample (X-T7) |
| COFUN "single most dangerous": does a neutral root dipole make f_0 grow? | open | **answered: no** (conditionally) | X1 with b = q·(one coarse link) |

## 8. Summary table (every claim in the batch; 77 verdict units)

| id | claim (file, locating string) | verdict |
|---|---|---|
| TQ1 | QN, Sigma Q_X = 0 (TENTQ l.127) | CONFIRMED |
| TQ2 | QSBP (*) (l.147) | CONFIRMED |
| TQ3 | Q_X != 0; |Q_X| <= 8 Sigma pi_l, attained (l.165-185) | CONFIRMED |
| TQ4 | QFALSE: (NEUT-box) false by L^{2k}, struck (l.189-209) | CONFIRMED (class-level; exact ratio (4/3)(n^2 - 1/n) with D^perp; l.201 arithmetic slip n^2 - 1 vs n^2 - 1/n; does not refute row-specific neutrality) |
| TQ5 | PINC (l.211) | CONFIRMED |
| TQ6 | TQ-INT; "box charges eliminated" (l.261-274) | CONFIRMED (identity; reformulation, not a gain) |
| TQ7a | TENT-TV l1 bound | CONFIRMED |
| TQ7b | TENT-TV pointwise |delta_mu| <= 15/(8n) (l.281) | REFUTED: 15 L^l/(8n), capped at 1 |
| TQ8 | TQ-NOGAIN "osc = max exactly" (l.304) | REFUTED: max <= osc <= 2 max |
| TQ9 | TGAUGE identity (l.321) | CONFIRMED |
| TQ10 | TQ (iii) calibration 130/6561; reduction to (TENT-osc) | CONFIRMED |
| TQ11 | §4.3 factor k upstream; Sigma pi_l gives k | CONFIRMED (spot) |
| YS1 | YS-K support/norms (l.123-160) | CONFIRMED at i = 0 (spot) |
| YS2 | "dimensionless and carries no k" (l.163) | REFUTED |
| YS3a | YS-AVG power n_i^{-2} | CONFIRMED (analytic) |
| YS3b | YS-AVG/YS-CORE constants 64, 96, 15.13 | NOT-VERIFIED (site vs link count, factor up to d) |
| YS4a | YS-CORE (ii) witness -65/26244, terminates | CONFIRMED (order-averaged h) |
| YS4b | "the very field BFT_A §38.7 takes as g_0" (l.230) | REFUTED (g_0 = d*(chi omega^p)) |
| YS5a | (TENT-osc) false by n^2 — class form | CONFIRMED |
| YS5b | (TENT-osc) false by n^2 — for the response (l.252-262) | NOT-VERIFIED |
| YS6 | "averaging does not beat the core"; i = 0 binding (l.272-284) | CONFIRMED (structural) |
| YS7 | YS-DEC (c) away from p's cell (l.286) | NOT-VERIFIED (ARGUED as labelled) |
| YS8 | YS-DEC (d) (Y-sup^loc) false by n | NOT-VERIFIED (plausible; conditional on the response core) |
| YS9 | YS-PHI ratio L^{-2} (l.308) | CONFIRMED |
| YS10 | YSUP l.249 normalisation erratum; 486/65 | CONFIRMED |
| YS11 | YS-GT / Hölder-fallback assessment (l.325-382) | NOT-VERIFIED (ARGUED as labelled) |
| FB1 | face (b) = (TENT-osc), n = L^k, square on neither leg | CONFIRMED |
| FB2a | FB-CLASS with 65/26244 (l.273) | CONFIRMED (order-averaged h; class Y only) |
| FB2b | FB-CLASS decimal 2.4768e-3 as a lower bound | REFUTED (overshoots by 89/2050312500) |
| FB3 | FB-NOEST (l.251) | REFUTED |
| FB4a | 243/260 = 93.46% (FB-LOCAL, l.449) | CONFIRMED (order-averaged h; 100% with fixed-order h) |
| FB4b | "any fix must change h_0" (l.454) | REFUTED |
| FB5 | FB-BOOT "no lower bound at all"; sign of G_e missing (l.304) | REFUTED |
| FB6 | "dimensionless => k-independent" (l.142, l.669) | REFUTED |
| FB7a | FB-ONE-LEG, trivial half | CONFIRMED |
| FB7b | FB-ONE-LEG, face (b) not binding / sigma term L^{2k-3} | NOT-VERIFIED |
| FB8a | price rows, k* = 160.380 | CONFIRMED (conditional on X1/X2, frozen constants) |
| FB8b | k* ~ 81.7 doubled currency (l.537) | REFUTED (80.940) |
| FB9 | FB-BIANCHI type claim (l.365-371) | REFUTED |
| FB10 | SHARP-AND-FATAL (l.685) | REFUTED (as a statement about f_0) |
| FB11 | fb1 gates | NOT-VERIFIED (not re-run) |
| GS1 | G_e construction | CONFIRMED |
| GS2 | GS-ZERO (l.192) | CONFIRMED (r = infinity admitted; Y^p r-free; not vacuous; T-caveat) |
| GS3 | 1/2 is a threshold (l.231) | CONFIRMED |
| GS4 | GS-ZS, GS-FM, GS-MOM (l.249-290) | CONFIRMED |
| GS5a | GS-WINDOW algebra (l.322) | CONFIRMED (pointwise) |
| GS5b | GS-WINDOW's adjudication of FB-BOOT | REFUTED (sup bound positive at eps = 1/2) |
| GS6 | GS-SHARP (l.370) | CONFIRMED as an implication (inputs open; T-caveat) |
| GS7a | K'_0 = 0 at BFT_A l.2761 | CONFIRMED |
| GS7b | GS-BASE "(CC-0) holds exactly" (l.461-476) | REFUTED (only (cc); r55t E2); conclusion survives via X1 |
| GS8 | GS-NOCIRC "not circular" (l.514) | NOT-VERIFIED |
| GS9 | GS-STEP (l.482) | CONFIRMED |
| GS10 | GS-ONELEG: FB-ONE-LEG upgraded to PROVEN (l.607) | REFUTED (as an upgrade) |
| GS11a | (R1) slice-preserving solve | CONFIRMED |
| GS11b | (R4) sufficiency "PROVEN-HERE" | NOT-VERIFIED |
| GS12 | g_0 / u correction | CONFIRMED |
| CF1 | target stale (l.160) | CONFIRMED |
| CF2a | three classes share the name | CONFIRMED |
| CF2b | D1's class is (cc) | CONFIRMED |
| CF2c | (CO-fun)[cc] FALSE as stated (l.155) | REFUTED (conditional on Theorem COF + LINEAR_PACKAGE Thm 4.2 (ii); X1) |
| CF3 | exponent window alpha in (0,1/2), theta_c in (alpha, 1-alpha] | CONFIRMED against the source (l.192's quote of BFT_A is wrong) |
| CF4a | ||h^T||_{1->1} = 8/3 | CONFIRMED |
| CF4b | ||h^T||_{inf->inf} = 1/3 "sharp", "3x", "dimension-blind" (l.249) | REFUTED for the lane's h (10/81; X-T6) |
| CF5 | handle 2: no hidden L^{k-l} | CONFIRMED |
| CF6 | Lemma CO-pin (l.389) | CONFIRMED |
| CF7a | relocation inequality, 0.3462 n^3 max|Q_X| (l.433) | CONFIRMED (upper bound; 5/39 with the lane's h) |
| CF7b | (ROOT-sup) false on the class | CONFIRMED |
| CF7c | (CO-fun)[cc] <= (YH-pin) and (ROOT-sup) | NOT-VERIFIED |
| CF7d | ">= 2dL^{-3}L^{-theta_c}||j||_Pc" (l.441) | REFUTED (must be <=) |
| CF7e | "second, independent route" | REFUTED (same object B) |
| CF8 | CO-pin discharges half of RS10-6; gauge side unobstructed (l.404) | REFUTED |
| CF9 | "no per-level sharpening can ever remove the k-factor" (l.487) | REFUTED (narrow form CONFIRMED) |
| CF10 | §5(a) Lemma CD gives (CC-0) or nothing (l.349) | REFUTED (reasoning; gives (cc)) |
| CF11 | erratum vs BFT_B l.3810 | CONFIRMED |
| CF12 | cf1 gates/provenance | NOT-VERIFIED (not re-run) |
| CF13 | j-hat_0 collision (Codex F14) | CONFIRMED |
| CF14 | D(S^s) = 0 unjustified at roots (Codex F15) | CONFIRMED (settled by r55t E2) |

**Counts: CONFIRMED 44 · NOT-VERIFIED 11 · REFUTED 22.** Plus three cross-cutting findings not in any
file: X-T6 (operator collision, CONFIRMED), X-T7 (top-level root charges; Lemma SPLIT's s-slot claim
false for the top slot, CONFIRMED by r55t E2), X1 (root charges of (cc) sources are data; PROVEN as an
implication, sup half, pending an independent check).

## 9. What the actual remaining obstruction in this neighbourhood is

The four successive files each named a different obstruction — the box charges and (NEUT-box) (TENTQ),
then (TENT-osc) at the core (YSUP), then face (b)'s n^2 and its "sign of G_e" and FB-NBHD circularity
(FACEB), then the G_e question dissolved but the circle re-cast (GESIGN), then (YH-pin) + (ROOT-sup)
(COFUN) — and **all of them are faces of one bookkeeping term**: Proposition COF-res's root-charge
residue, which exists only because Theorem COF's proof splits f_0 into a "covered" part and that
residue. That residue is not an obstruction to the curvature half: a composite-co-closed source's root
charges are the divergence of a level-k current b with ||b||_inf <= Sigma_l pi_l (max-flow on the
coarse torus, with the cut bound coming straight from the source's own fluxes), and Q_{k-1}^T b is
literally a datum B_k = b/kappa_{k-1}, whose curvature LINEAR_PACKAGE Theorem 4.2 (ii) already bounds
k- and T-uniformly; what is left is (CC-0) and Theorem COF covers it (X1; conditional on those two
banked theorems, sup half only, not yet independently checked). What remains in this neighbourhood is
therefore two things, neither of which any of the five files is about. **First, upstream and binding
everywhere: the level count.** Applied to the contraction's rows, both Theorem COF's class norm and
X1's flux potential cost Sigma_l pi_l(V_l), i.e. about k times the per-level row size (S10-6/RS10-1;
TENTQ §4.3), and at fixed Hölder exponent the theta-optimisation that would soften it is not available
(Codex COFUN F11.2); removing it needs lane A's (SPD)/(W2), OPEN. **Second, off the critical set for
Gamma_E: the off-root divergence D^perp(S)** — face (a), not face (b): the gauge-fixing remainder
n^2<D^perp(S), lambda^{Gamma_E}_*(p)> of Proposition NCR, equivalently the (P0)-slot size of the slice
correction Gamma_E^T D(S) (TENTQ's (P0-sup)). Its l^inf x l1 route is dead ((Y-sup^loc) fails by n;
GT-ell's first term loses n), and its only live route is YSUP's dipole-convolution argument (YS-GT,
ARGUED; it needs the Neumann box Green's-gradient profile |A^X_w(b)| <~ |b - w|^{-3} and a pricing of the
D^perp factor in the source's own currency, TENTQ §5 item 4). Secondary items to close the curvature
half on (cc) completely: the Hölder half of X1 (a Hölder bound for the data-to-f_0 map), and the
X-T7 text repairs (Lemma SPLIT's top residual slot; §35.6's reading of Lemma CD at the roots).

## 10. For the lead: what should change in PROOF.md's tally / HANDOFF's critical path (no file edited)

1. **(CO-fun)[cc] must not be carried as FALSE.** At minimum OPEN (the falsity argument is term-level;
   Codex COFUN F2/F7 agree); with X1, its sup half is PROVEN as an implication of Theorem COF and
   LINEAR_PACKAGE Theorem 4.2 (ii). Request an independent hostile check of X1 (it reverses S10-11).
2. **Remove from the critical path:** (TENT-Q), (TENT-osc), "face (b)", the sign of G_e, FB-NBHD's
   circularity, (YH-pin), (ROOT-sup). Keep their exact statements as facts about COF-res's bookkeeping.
3. **(NEUT-box) stays struck** (class-false by exactly n^2, not needed, not sufficient), but must not be
   cited as evidence that root/box neutrality routes are risky.
4. **Operator erratum (X-T6):** BFT_B §27.1 l.3589 and §29.2 l.3696 should read "averaged over the 4!
   coordinate orders (LINEAR_PACKAGE §1.2)". COFUN's "sharp 1/3" and "dimension-blind" are for the wrong
   operator (lane's value 10/81, d-dependent); witness constants 65/26244 and 243/260 are correct for the
   lane's operator only.
5. **Top-level root charges (X-T7):** Lemma SPLIT's "D(S^s) = 0" is false for a non-co-closed top
   residual slot (r55t E2); repair by reclassifying Q^T s_{k-1} as a plain current before citing Theorem
   COF. §35.6/Theorem NCE (i)'s "(CC-0) at critical points, roots included" is not given by Lemma CD
   (root values kappa_{k-1}(d* r_{k-1}(x;B))(X)). GESIGN GS-BASE's "(CC-0) exactly at x_0 = 0" is false;
   its conclusion survives via X1.
6. **Critical path in this neighbourhood:** (SPD)/(W2) (the level count) upstream; off the critical set,
   the off-root divergence D^perp — the gauge-fixing remainder n^2<D^perp, lambda^{Gamma_E}_*> /
   (P0-sup) — with YSUP's YS-GT as the only live route (ARGUED).
7. Numeric corrections: 81.7 -> 80.940 (FACEB l.537); 2.4768e-3 -> 65/26244 (or 0.0024767) as a lower
   bound; YSUP l.249's psi_u for the un-normalised u is -130/6561; COFUN l.441 ">=" -> "<="; TENTQ l.201
   n^2 - 1 -> n^2 - 1/n (bound unaffected); TENTQ l.281 15/(8n) -> 15 L^l/(8n).

UTC at end: 2026-10-28T22:58Z. Files written by this reviewer: this file; checks/r55t_criteria.md,
checks/r55t_checks.py, checks/r55t_out.txt, checks/r55t_err.txt; scratch r55t_rows.txt in the session
scratchpad (row count only). No git command was run; no other lane file was edited.
